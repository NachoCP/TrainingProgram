import streamlit as st

def add_course():
    # Verificar si la configuración está completa
    if not st.session_state.get("config_done", False):
        st.error("Primero debes completar la configuración inicial.")
        st.stop()

    st.title("Añadir Cursos")
    
    # Lógica para añadir cursos
    st.write("Formulario para añadir cursos.")
