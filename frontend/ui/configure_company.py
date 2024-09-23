import streamlit as st


def company_view():
    st.title("Configure Company")

    # Inputs para ingresar el nombre y propósito de la compañía
    name = st.text_input("Introduce a company name")
    purpose = st.text_area("Enter the purpose of the company")


    # Guardar automáticamente los inputs en el session_state
    st.session_state['company_name'] = name
    st.session_state['company_purpose'] = purpose

    # Help icon with an expandable text for additional information
    with st.expander("ℹ️ Why is this important?"):
        st.write("""
            The entire description will be used for generating synthetic data, so make sure to be as explicit and detailed as possible.
            Include information like mission, vision, values, and objectives of the company.
            """)
    # Comprobamos si se ha completado la configuración
    if "config_none" not in st.session_state:
        st.session_state.config_done = False


    # Botón para guardar la configuración
    if st.button("Generate Competencies"):
        if name and purpose:
            st.session_state.page = "competencies_view"
            st.rerun()
        else:
            st.error("Please, fill all the fields in order to continue with the configuration")
