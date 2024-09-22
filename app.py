import streamlit as st
from frontend.ui.manager_view import manager_options
from frontend.ui.add_course import add_course
from frontend.ui.configure_company import company_interactions

def main():
    # Asegurar que la configuración está en session_state
    if 'config_done' not in st.session_state:
        st.session_state.config_done = False

    # Mostrar barra lateral según el estado
    if not st.session_state.config_done:
        st.sidebar.title("Configuración Inicial")
        company_interactions()  # Mostrar solo la página de configuración
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
