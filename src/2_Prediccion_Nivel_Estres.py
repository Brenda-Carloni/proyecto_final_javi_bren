import streamlit as st
import os
from pickle import load
import pandas as pd


st.set_page_config(page_title="Sistema de Predicción de Nivel de Estrés", page_icon="🧠", layout="wide")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta_modelo = os.path.join(BASE_DIR, "../models/modelo_random_forest_42.sav")

modelo = load(open(ruta_modelo, "rb"))
clases = {
    "0": "Bajo",
    "1": "Medio",
    "2": "Alto",
    "3": "Muy Alto"
}

st.markdown(
    """
    <style>
    .stApp {
        background-color: #FCF4F0;
        --primary-color: #D87093 !important;
    }
    header[data-testid="stHeader"] {
        background-color: transparent;
    }
    section[data-testid="stSidebar"] {
        background-color: #FAE1F0;
    }
    div[data-baseweb="slider"] [role="slider"] {
        background-color: #D87093 !important;
        border-color: #D87093 !important;
        box-shadow: none !important;
    }
    div[data-baseweb="slider"] div[data-testid="stSliderTrack"] > div {
        background-color: #D87093 !important;
    }
    div[data-testid="stSlider"] div[data-testid="stMarkdownContainer"] p {
        color: #D87093 !important;
    }
    div.stButton > button {
        background-color: #D87093 !important; /* Color de fondo del botón */
        color: #FFFFFF !important;            /* Color del texto del botón */
        border: 1px solid #D87093 !important; /* Color del borde */
        border-radius: 8px !important;        /* Bordes redondeados */
        font-weight: bold !important;         /* Texto en negrita */
    }
    div.stButton > button:hover {
        background-color: #C75B80 !important;
        border-color: #C75B80 !important;
        color: #FFFFFF !important;
    }
    div.stButton > button:active {
        background-color: #B5476E !important;
        color: #FFFFFF !important;
    
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🧠 Sistema de Predicción de Nivel de Estrés")
st.write("Completa la información del estudiante a continuación.")
st.divider()

st.subheader("👤 Información del Estudiante")
c1, c2 = st.columns(2)

with c1:
    Horas_Diarias_Promedio_de_RRSS = st.slider("Horas Diarias Promedio de RRSS", min_value = 0.0, max_value = 24.0, step = 0.1)
    Horas_Diarias_Promedio_de_Estudio = st.slider("Horas Diarias Promedio de Estudio", min_value = 0.0, max_value = 24.0, step = 0.1)
    Horas_Diarias_Promedio_de_Actividad_Física = st.slider("Horas Diarias Promedio de Actividad Física", min_value = 0.0, max_value = 24.0, step = 0.1)
    Horas_Diarias_Promedio_de_Sueño_Por_Noche = st.slider("Horas Diarias Promedio de Sueño Por Noche", min_value = 0.0, max_value = 24.0, step = 0.1)
    Puntaje_de_Salud_Mental = st.slider("Percepción de Salud Mental (puntaje de 0 a 10)", min_value = 0.0, max_value = 10.0, step = 0.1)


st.divider()

if st.button("🔍 Predecir Nivel de Estrés", use_container_width=True):
    prediccion = str(modelo.predict([[Horas_Diarias_Promedio_de_RRSS,
                                      Horas_Diarias_Promedio_de_Estudio,
                                      Horas_Diarias_Promedio_de_Actividad_Física,
                                      Horas_Diarias_Promedio_de_Sueño_Por_Noche,
                                      Puntaje_de_Salud_Mental]])[0])
    pred_clases = clases[prediccion]

  
    st.divider()
    st.subheader("🧠 Resultados de la Predicción")
    
    if prediccion == "0": 
        st.success("💚 El nivel de estrés del estudiante es **BAJO**. \n\n Esto indica que el estudiante tiene un buen manejo del estrés y está en un estado emocional saludable. Los resultados sugieren un nivel de estrés reducido, asociado a una situación en la que podría existir un buen equilibrio entre las actividades académicas, el descanso y el bienestar personal. Se recomienda mantener estos hábitos y continuar prestamdo atención al equilibrio entre estudio, descanso y tiempo personal.")
    elif prediccion == "1":  # Medio (Azul/Informativo)
        st.warning("⚠️ El nivel de estrés del estudiante es **MEDIO**. \n\n Los resultados sugieren la presencia de un nivel de estrés moderado, que puede estar relacionado con las exigencias académicas y las actividades cotidianas. Se recomienda mantener una adecuada organización del tiempo, procurar un descanso suficiente y reservar momentos para actividades de recreación y bienestar personal.")
    elif prediccion == "2":  # Alto (Naranja/Advertencia)
        st.error("🚨 El nivel de estrés del estudiante es **ALTO**. \n\n Los resultados indican una mayor presencia de factores asociados al estrés. Puede ser útil revisar los hábitos de estudio, descanso y actividad física diaria, así como identificar aquellas situaciones que puedan estar generando mayor presión. Si este nivel de estrés se mantiene o afecta el bienestar cotidiano, se recomienda considerar la posibilidad de buscar orientación o apoyo.")
    elif prediccion == "3":  # Muy Alto (Rojo/Error)
        st.error("🚨 El nivel de estrés del estudiante es **MUY ALTO**. \n\n Los resultados indican una presencia elevada de factores asociados al estrés. Se recomienda prestar especial atención al bienestar personal, revisar las demandas académicas y cotidianas y procurar espacios adecuados de descanso y recuperación. Si la situación genera malestar persistente o interfiere con la vida cotidiana, puede ser conveniente buscar orientación de un profesional de la salud.")