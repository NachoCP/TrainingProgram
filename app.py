import streamlit as st

from frontend.services.department import DepartmentService
from frontend.services.employee import EmployeeService
from frontend.ui.add_course import add_course
from frontend.ui.configure_company_view import company_view
from frontend.ui.configure_entities_view import entities_view
from frontend.ui.employee_view import employee_view


def main():
    # Asegurar que la configuración está en session_state
    if "config_done" not in st.session_state:
        st.session_state.config_done = False

    if "page" not in st.session_state:
        st.session_state.page = "company_view"

    # Mostrar barra lateral según el estado
    if not st.session_state.config_done:
        if st.session_state.page == "company_view":
            company_view()
        elif st.session_state.page == "entities_view":
            entities_view()
    else:
        st.sidebar.title("Navigate")
        departments = DepartmentService().get_list()

        options_dep = [department.name for department in departments]
        choice_department = st.sidebar.selectbox("Select the department", options_dep)

        st.session_state.department = next((item for item in departments if item.name == choice_department), None)
        employees = EmployeeService().get_list_by_department(st.session_state.department.id)

        options_employee = [employee.name for employee in employees]
        choice_employee = st.sidebar.selectbox("Select the employee", options_employee)

        st.session_state.employee = next((item for item in employees if item.name == choice_employee), None)

        employee_view()

# Llama a la función principal al iniciar la aplicación
if __name__ == "__main__":
    main()
