import streamlit as st

def company_interactions():
    st.title("Configurar Compañía")

    # Inputs para ingresar el nombre y propósito de la compañía
    name = st.text_input("Nombre de la Compañía")
    purpose = st.text_input("Propósito de la Compañía")

    # Comprobamos si se ha completado la configuración
    if 'config_done' not in st.session_state:
        st.session_state.config_done = False

    # Botón para guardar la configuración
    if st.button("Guardar Configuración"):
        if name and purpose:
            # Cambiamos el estado a True cuando se completa la configuración
            st.session_state.config_done = True
            st.success("Configuración completada con éxito.")
            st.write(f"Compañía: {name}")
            st.write(f"Propósito: {purpose}")
            st.rerun()
        else:
            st.error("Por favor, completa todos los campos.")
