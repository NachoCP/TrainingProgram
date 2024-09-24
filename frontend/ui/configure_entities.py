import time

import pandas as pd
import streamlit as st

from commons.models.core.competency import Competency
from commons.models.core.department import Department
from commons.models.core.employee import EmployeeWithoutDates
from frontend.services.competency import CompetencyService
from frontend.services.competency_level import CompetencyLevelService
from frontend.services.course import CourseService
from frontend.services.department import DepartmentService
from frontend.services.employee import EmployeeService
from frontend.services.employee_competency import EmployeeCompetencyService
from frontend.services.employee_department import EmployeeDepartmentService
from frontend.services.feedback import FeedbackService
from frontend.synthetic.synthetic_llm import DataSyntheticLLM


def update_competency(competency_id, new_name, new_description):
    for comp in st.session_state.competencies:
        if comp.id == competency_id:
            comp.name = new_name
            comp.description = new_description
            break

def competencies_view():

    st.title("Competencies View")
    st.markdown("""Format table will all the competencies, deparments and employees that has been synthetic generated
                using an LLM. Please feel free to add any new competency to the list or modify existing ones.
                When you feel ready click "Load Config" to start the process of generating all the data.
                """)

    if "data_loaded" not in st.session_state:
    # Simulamos la generación de competencias con datos sintéticos
        name = st.session_state['company_name']
        purpose =st.session_state['company_purpose']
        num_competencies = 10
        num_employees = 20
        num_departments = 5
        preamble = f"{name} \n {purpose}"
        with st.spinner('Generating synthetic data...'):
            st.session_state.competencies = DataSyntheticLLM(Competency).create(num=num_competencies, preamble=preamble)
            st.session_state.employees = DataSyntheticLLM(EmployeeWithoutDates).create(num=num_employees, preamble=preamble)
            st.session_state.departments = DataSyntheticLLM(Department).create(num=num_departments, preamble=preamble)
            st.session_state.data_loaded = True

        st.success("Data successfully generated!")

    df_competencies = pd.DataFrame([competency.model_dump() for competency in st.session_state.competencies])
    df_employees = pd.DataFrame([employee.model_dump() for employee in st.session_state.employees])
    df_departments = pd.DataFrame([department.model_dump() for department in st.session_state.departments])

    st.markdown("## **Competency Table**")
    edited_df_competencies = st.data_editor(df_competencies, num_rows="dynamic")
    st.markdown("## **Employee Table**")
    edited_df_employees = st.data_editor(df_employees, num_rows="dynamic")
    st.markdown("## **Departments Table**")
    edited_df_departments = st.data_editor(df_departments, num_rows="dynamic")

    if st.button("Load Config"):
        department_ids =[department["id"] for department in edited_df_departments.to_dict("records")]
        employee_ids = [employee["id"] for employee in edited_df_employees.to_dict("records")]
        competency_ids = [competency["id"] for competency in edited_df_competencies.to_dict("records")]

        with st.spinner('Inserting synthetic data...'):
                EmployeeService().send_bulk(edited_df_employees.to_dict("records"))
                DepartmentService().send_bulk(edited_df_departments.to_dict("records"))
                CompetencyService().send_bulk(edited_df_competencies.to_dict("records"))
                time.sleep(10)
                CourseService().send_bulk()
                FeedbackService().send_bulk(employee_ids)
                CompetencyLevelService().send_bulk(competency_ids, department_ids)
                EmployeeCompetencyService().send_bulk(competency_ids, employee_ids)
                EmployeeDepartmentService().send_bulk(department_ids, employee_ids)

        st.success("Loaded Successfully all the entities")
