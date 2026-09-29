import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset", page_icon="📊", layout="wide")

st.title("📊 Student Social Media And Mental Health Impact")

df = pd.read_csv("data/raw/Student Social Media And Mental Health Impact.csv")

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