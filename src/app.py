import streamlit as st

st.set_page_config(
    page_title="Sistema de Predicción de Nivel de Estrés",
    page_icon="🧠",
    layout="wide"
)

inicio = st.Page("1_Inicio.py", title="Inicio", icon="🏠", default=True)
prediccion = st.Page("2_Prediccion_Nivel_Estres.py", title="Predicción de Nivel de Estrés", icon="🧠")
dataset = st.Page("3_Dataset.py", title="Exploración del Dataset", icon="📈")
acerca = st.Page("4_Acerca.py", title="Acerca de Este Proyecto", icon="ℹ️")

pg = st.navigation(
    {
        "General": [inicio],
        "Módulos del Proyecto": [prediccion, dataset, acerca],
    }
)
pg.run()
    



