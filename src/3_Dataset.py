import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Dataset", page_icon="📊", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #FCF4F0;
    }
    header[data-testid="stHeader"] {
        background-color: transparent;
    }
    section[data-testid="stSidebar"] {
        background-color: #FAE1F0;
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

st.title("📊 Student Social Media And Mental Health Impact")

BASE_DIR = Path(__file__).resolve().parent.parent

csv_path = (
    BASE_DIR
    / "data"
    / "raw"
    / "Student Social Media And Mental Health Impact.csv"
)

df = pd.read_csv(csv_path)

st.subheader("Vista Previa del Conjunto de Datos")
st.dataframe(df, use_container_width=True)

st.subheader("Formato del Conjunto de Datos")

col1, col2 = st.columns(2)

with col1:
    st.metric("Filas", df.shape[0])

with col2:
    st.metric("Columnas", df.shape[1])

st.subheader("Tipos de Datos de las Columnas")
st.dataframe(df.dtypes.astype(str))

st.subheader("Resumen de Estadísticas")
st.dataframe(df.describe())

st.download_button(
    "⬇ Descargar Conjunto de Datos",
    data=df.to_csv(index=False),
    file_name="Student Social Media And Mental Health Impact.csv",
    mime="text/csv"
)