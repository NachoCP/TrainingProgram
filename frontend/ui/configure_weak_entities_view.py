import pandas as pd
import streamlit as st

from frontend.services.competency import CompetencyService
from frontend.services.competency_level import CompetencyLevelService
from frontend.services.department import DepartmentService
from frontend.services.employee import EmployeeService
from frontend.services.employee_competency import EmployeeCompetencyService
from frontend.services.employee_department import EmployeeDepartmentService
from frontend.services.feedback import FeedbackService
from frontend.synthetic.generation import (
    get_competency_levels,
    get_employee_competencies,
    get_employee_departments,
    get_feedbacks,
)
from frontend.utils.enum import ViewEnum


def weak_entities_view():

    st.title("Weak Entities View")
    st.markdown(
        """Format table will all the feedback, relationship between employee-competencies and
                employee-departments, and all the competency levels setted up for the different departments.
                Please feel free to add any new value  or modify existing ones.
                When you feel ready click "Next" to continue the configuration process.
                """
    )
    competencies = CompetencyService().get_list()
    departments = DepartmentService().get_list()
    employees = EmployeeService().get_list()

    department_ids = [department.id for department in departments]
    employee_ids = [employee.id for employee in employees]
    competency_ids = [competency.id for competency in competencies]

    if "data_loaded_weak" not in st.session_state:
        st.session_state.data_loaded_weak = False
    # st.session_state.data_loaded_weak = False

    if not st.session_state.data_loaded_weak:

        with st.spinner("Generating synthetic data..."):
            st.session_state.feedbacks = get_feedbacks(employee_ids)
            st.session_state.competency_levels = get_competency_levels(competency_ids, department_ids)
            st.session_state.employee_competencies = get_employee_competencies(employee_ids, competency_ids)
            st.session_state.employee_departments = get_employee_departments(department_ids, employee_ids)
            st.session_state.data_loaded_weak = True

        st.success("Data successfully generated!")

    df_competencies = pd.DataFrame([competency.model_dump() for competency in competencies])
    df_employees = pd.DataFrame([employee.model_dump() for employee in employees])
    df_departments = pd.DataFrame([department.model_dump() for department in departments])
    df_feedbacks = pd.DataFrame([feedback.model_dump() for feedback in st.session_state.feedbacks])
    df_competency_levels = pd.DataFrame(
        [competency_level.model_dump() for competency_level in st.session_state.competency_levels]
    )
    df_employee_competencies = pd.DataFrame(
        [employee_competency.model_dump() for employee_competency in st.session_state.employee_competencies]
    )
    df_employee_department = pd.DataFrame(
        [employee_department.model_dump() for employee_department in st.session_state.employee_departments]
    )

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Feedback Table", "Employee Competencies Table", "Employee Department Table", "Competency Levels Table"]
    )

    df_final_feedback = (
        df_feedbacks.merge(df_employees, left_on="employee_id", right_on="id", how="left", suffixes=("", "_employee"))
        .drop("id_employee", axis=1)
        .merge(df_employees, left_on="feedback_by", right_on="id", how="left", suffixes=("", "_feedback_by"))
        .drop("id_feedback_by", axis=1)
        .rename(columns={"name": "employee_name", "name_feedback_by": "employee_feedback_by_name"})
    )[
        [
            "id",
            "employee_id",
            "employee_name",
            "feedback_by",
            "employee_feedback_by_name",
            "comments",
            "score",
            "effective_date",
        ]
    ]
    # print(df_final_feedback)

    df_final_employee_competencies = (
        df_employee_competencies.merge(
            df_employees, left_on="employee_id", right_on="id", how="left", suffixes=("", "_employee")
        )
        .drop("id_employee", axis=1)
        .merge(df_competencies, left_on="competency_id", right_on="id", how="left", suffixes=("", "_competency"))
        .drop("id_competency", axis=1)
        .rename(columns={"name": "employee_name", "name_competency": "competency_name"})
    )[["id", "employee_id", "employee_name", "competency_id", "competency_name", "current_level"]]

    df_final_employee_department = (
        df_employee_department.merge(
            df_employees, left_on="employee_id", right_on="id", how="left", suffixes=("", "_employee")
        )
        .drop("id_employee", axis=1)
        .merge(df_departments, left_on="department_id", right_on="id", how="left", suffixes=("", "_department"))
        .drop("id_department", axis=1)
        .rename(columns={"name": "employee_name", "name_department": "department_name"})
    )[["id", "employee_id", "employee_name", "department_id", "department_name"]]

    df_final_competency_levels = (
        df_competency_levels.merge(
            df_competencies, left_on="competency_id", right_on="id", how="left", suffixes=("", "_competency")
        )
        .drop("id_competency", axis=1)
        .merge(df_departments, left_on="department_id", right_on="id", how="left", suffixes=("", "_department"))
        .drop("id_department", axis=1)
        .rename(columns={"name": "competency_name", "name_department": "department_name"})
    )[["id", "competency_id", "competency_name", "department_id", "department_name", "required_level", "num_workers"]]

    with tab1:
        edited_feedback = st.data_editor(df_final_feedback, num_rows="dynamic")
    with tab2:
        edited_df_competency_levels = st.data_editor(df_final_competency_levels, num_rows="dynamic")
    with tab3:
        edited_df_employee_department = st.data_editor(df_final_employee_department, num_rows="dynamic")
    with tab4:
        edited_df_employee_competencies = st.data_editor(df_final_employee_competencies, num_rows="dynamic")

    if st.button("Next"):

        with st.spinner("Inserting synthetic data for weak entities..."):

            FeedbackService().send_bulk(edited_feedback.to_dict("records"))
            CompetencyLevelService().send_bulk(edited_df_competency_levels.to_dict("records"))
            EmployeeCompetencyService().send_bulk(edited_df_employee_competencies.to_dict("records"))
            EmployeeDepartmentService().send_bulk(edited_df_employee_department.to_dict("records"))

            st.success("Loaded Successfully all the entities")
            st.session_state.page = ViewEnum.employee_view
            st.rerun()
