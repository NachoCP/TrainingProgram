import streamlit as st

from frontend.ui.add_course import add_course
from frontend.ui.configure_company import company_view
from frontend.ui.configure_entities import competencies_view
from frontend.ui.manager_view import manager_options


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
        elif st.session_state.page == "competencies_view":
            competencies_view()
    else:
        st.sidebar.title("Navegación")
        options = ["Dashboard de Empleados", "Opciones del Manager"]
        choice = st.sidebar.selectbox("Selecciona una página", options)

        if choice == "Add Course":
            add_course()
        elif choice == "Opciones del Manager":
            manager_options()

# Llama a la función principal al iniciar la aplicación
if __name__ == "__main__":
    main()
