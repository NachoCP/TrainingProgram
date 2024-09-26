import json
import time

import pandas as pd
import streamlit as st

from commons.constants import COURSE_DEFAULT_DIR_DATA
from commons.models.core.competency import Competency
from commons.models.core.department import Department
from commons.models.core.employee import EmployeeWithoutDates
from frontend.services.competency import CompetencyService
from frontend.services.course import CourseService
from frontend.services.department import DepartmentService
from frontend.services.employee import EmployeeService
from frontend.synthetic.synthetic_llm import DataSyntheticLLM
from frontend.utils.enum import ViewEnum


def strong_entities_view():

    st.title("Strong Entities View")
    st.markdown("""Format table will all the competencies, deparments and employees that has been synthetic generated
                using an LLM. Please feel free to add any new competency to the list or modify existing ones.
                When you feel ready click "Next" to bulk this data and see the week entities generation view.
                """)

    if "data_loaded" not in st.session_state:

        name = st.session_state["company_name"]
        purpose =st.session_state["company_purpose"]
        num_competencies = 10
        num_employees = 20
        num_departments = 5
        preamble = f"{name} \n {purpose} \n"
        with st.spinner("Generating synthetic data..."):
            st.session_state.competencies = DataSyntheticLLM(Competency).create(num=num_competencies, preamble=preamble + "Please generate competencies that are associated with the company.")
            st.session_state.employeess = DataSyntheticLLM(EmployeeWithoutDates).create(num=num_employees, preamble=preamble + "Generate the user as Firstname Lastname.")
            st.session_state.departments = DataSyntheticLLM(Department).create(num=num_departments, preamble=preamble + "Generate departments associated with a real use case of a company.")
            st.session_state.data_loaded = True

        st.success("Data successfully generated!")

    df_competencies = pd.DataFrame([competency.model_dump() for competency in st.session_state.competencies])
    df_employees = pd.DataFrame([employee.model_dump() for employee in st.session_state.employeess])
    df_departments = pd.DataFrame([department.model_dump() for department in st.session_state.departments])

    tab1, tab2, tab3, tab4 = st.tabs(["Competency Table", "Departments Table", "Employee Table", "Course JSON"])
    with tab1:
        edited_df_competencies = st.data_editor(df_competencies, num_rows="dynamic")
    with tab2:
        edited_df_departments = st.data_editor(df_departments, num_rows="dynamic")
    with tab3:
        edited_df_employees = st.data_editor(df_employees, num_rows="dynamic")
    with tab4:
        st.write("Json information showed as table with all the courses used."
                 "This courses are going to be enrich and ingest in the Vector Database")
        with open(COURSE_DEFAULT_DIR_DATA) as f:
            data_json = json.load(f)
        st.dataframe(pd.DataFrame(data_json))

    if st.button("Next"):
        st.session_state.competencies = edited_df_departments.to_dict("records")
        st.session_state.employeess = edited_df_employees.to_dict("records")
        st.session_state.departments = edited_df_competencies.to_dict("records")

        with st.spinner("Inserting synthetic data from strong entities..."):
            EmployeeService().send_bulk(edited_df_employees.to_dict("records"))
            DepartmentService().send_bulk(edited_df_departments.to_dict("records"))
            CompetencyService().send_bulk(edited_df_competencies.to_dict("records"))
            time.sleep(3)
            CourseService().send_bulk()
            st.success("Loaded Successfully all the entities")
            st.session_state.page = ViewEnum.weak_entities_view
            st.rerun()
