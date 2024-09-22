import streamlit as st

def manager_options():
    # Verificar si la configuración está completa
    if not st.session_state.get("config_done", False):
        st.error("Primero debes completar la configuración inicial.")
        st.stop()

    st.title("Dashboard de Empleados")
    
    # Lógica del dashboard
    st.write("Aquí iría el dashboard.")
