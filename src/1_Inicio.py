import streamlit as st

st.title("🧠 Sistema de Predicción de Nivel de Estrés")

st.markdown("---")

st.header("Bienvenido")

st.write("""
Esta aplicación predice el nivel de estrés de los estudiantes utilizando un modelo de Machine Learning
entrenado con datos de estudiantes.

El objetivo de este proyecto es demostrar el flujo de trabajo de aprendizaje automático, desde el procesamiento
de datos y la ingeniería de características hasta el entrenamiento y despliegue del modelo mediante Streamlit.
""")

st.subheader("Lo que puedes hacer con esta aplicación")

col1, col2 = st.columns(2)

with col1:
    st.success("""
✅ Predecir el Nivel de Éstres de un estudiante

✅ Ver la información del dataset utilizado para entrenar el modelo

✅ Aprender acerca del proyecto
""")

with col2:
    st.info("""
📊 Random Forest Classifier

📈 Predicción en Machine Learning 

⚡ Predicción en Tiempo Real
""")

st.markdown("---")


st.subheader("📚 Información del Estudiante Utilizada")

col3, col4 = st.columns(2)

with col3:
    st.write("""
- Horas Diarias Promedio de Pantalla
- Horas Diarias Promedio de Estudio
- Horas Diarias Promedio de Actividad Física
- Horas Diarias Promedio de Sueño
- Puntaje de Salud Mental
""")

st.markdown("---")

st.subheader("⚙️ Machine Learning Workflow")

st.markdown("""""")

st.markdown("---")


st.subheader("📌 Entendiendo la Predicción")

st.info("""
**Nivel de Estrés** representa el nivel de estrés que tiene un estudiante según el modelo, basado en patrones aprendidos
a partir de datos de estudiantes.

A mayor nivel de estrés indica que el estudiante puede estar experimentando un mayor nivel de presión o ansiedad, 
mientras que un nivel más bajo sugiere que el estudiante puede estar manejando mejor el estrés.

**Nota:** Esta predicción es generada por un modelo de Aprendizaje Automático y debería ser considerada
una estimación educativa en lugar de un diagnóstico médico. Siempre consulta con un profesional de la salud
calificado para una evaluación clínica y tratamiento.
""")

st.markdown("---")


st.caption("Desarrollado usando Python • Scikit-learn • Streamlit")