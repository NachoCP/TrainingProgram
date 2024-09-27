import pandas as pd
import streamlit as st

from frontend.services.competency_level import CompetencyLevelService
from frontend.services.department import DepartmentService
from frontend.services.employee import EmployeeService
from frontend.services.employee_competency import EmployeeCompetencyService
from frontend.ui.factory import ViewFactory
from frontend.utils.enum import ViewEnum


def main():
    # Asegurar que la configuración está en session_state

    if "page" not in st.session_state:
        st.session_state.page = "company_view"

    view = ViewFactory().get_view(st.session_state.page)
    if st.session_state.page == ViewEnum.employee_view.value:
        st.sidebar.title("Navigate")
        departments = DepartmentService().get_list()

        options_dep = [department.name for department in departments]
        choice_department = st.sidebar.selectbox("Select the department", options_dep)

        st.session_state.department = next((item for item in departments if item.name == choice_department), None)
        employees = EmployeeService().get_list_by_department(st.session_state.department.id)

        expected_competency_levels_department = CompetencyLevelService().get_all_by_department(
            st.session_state.department.id
        )
        real_competency_levels_department = EmployeeCompetencyService().get_all_group_department(
            st.session_state.department.id
        )

        df_expected_competency_levels_department = pd.DataFrame(
            [d.model_dump() for d in expected_competency_levels_department]
        )
        df_real_competency_levels_department = pd.DataFrame([d.model_dump() for d in real_competency_levels_department])

        df_merged_levels = df_expected_competency_levels_department.merge(
            df_real_competency_levels_department,
            on=["name", "required_level"],
            how="outer",
            suffixes=('_expected', '_real'),
        )

        df_merged_levels["num_workers_expected"] = df_merged_levels["num_workers_expected"].fillna(0)
        df_merged_levels["num_workers_real"] = df_merged_levels["num_workers_real"].fillna(0)
        df_merged_levels["diff_num_workers"] = df_merged_levels["num_workers_real"] - df_merged_levels[
            "num_workers_expected"
        ].astype(int)
        df_merged_levels = df_merged_levels[df_merged_levels["diff_num_workers"].astype(int) < 0]
        df_merged_levels["diff_num_workers"] = abs(df_merged_levels["diff_num_workers"])
        df_merged_levels = df_merged_levels.rename(
            columns={"name": "Competency", "required_level": "Level", "diff_num_workers": "Needed"}
        )
        options_employee = [employee.name for employee in employees]
        choice_employee = st.sidebar.selectbox("Select the employee", options_employee)

        st.session_state.employee = next((item for item in employees if item.name == choice_employee), None)

        st.sidebar.subheader("Uncovered competency levels")
        st.sidebar.dataframe(
            df_merged_levels[["Competency", "Level", "Needed"]], hide_index=True, use_container_width=True
        )
    view()


# Llama a la función principal al iniciar la aplicación
if __name__ == "__main__":
    main()
