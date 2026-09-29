import streamlit as st

st.set_page_config(
    page_title="Acerca del Proyecto",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ Acerca del Proyecto")
st.markdown("---")

st.markdown("""
## 🧠 Sistema de Predicción de Nivel de Estrés

Bienvenido al **Sistema de Predicción de Nivel de Estrés**, un proyecto de Machine Learning de extremo a extremo 
desarrollado para demostrar habilidades prácticas en Análisis de Datos, Ingeniería de Datos, Machine Learning,
Inteligencia de Negocios y Desarrollo de Aplicaciones Web.

Esta aplicación predice el nivel de estrés de un estudiante utilizando información de hábitos y presenta los 
resultados a través de una interfaz simple e interactiva de Streamlit.
""")

st.subheader("🔄 Flujo de Trabajo")

st.markdown("""""")

st.subheader("🛠️ Habilidades Demostradas")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
- ✅ Programación en Python
- ✅ Análisis de Datos con Pandas y NumPy
- ✅ Visualización de Datos con Matplotlib y Seaborn
- ✅ Limpieza de Datos
- ✅ Ingeniería de Características
- ✅ SQL (SQL3)

""")

with col2:
    st.markdown("""
- ✅ Análisis de Datos Exploratorio (EDA)
- ✅ Machine Learning
- ✅ Modelos de Clasificación (Random Forest Classifier)
- ✅ Evaluación de Modelos de Machine Learning
- ✅ Aplicación Web con Streamlit
""")

st.subheader("💻 Tecnologías Usadas")

st.markdown("""
| Categoría | Tecnología |
|-----------|------------|
| Programación | Python |
| Análisis de Datos | Pandas, NumPy |
| Visualización | Matplotlib, Seaborn |
| Base de Datos | SQL3 |
| Machine Learning | Scikit-learn |
| Guardado y Carga de Modelos | Pickle |
| App Web | Streamlit |
""")

st.warning("""
### ⚠️ Proyecto Educativo y de Portafolio

Esta aplicación fue desarrollada **únicamente con fines educativos y para mostrar nuestras habilidades** en 
análisis de datos, Machine Learning, SQL y Streamlit.

**NO** ha sido validado clínicamente.
""")

st.error("""
### 🚨 Aviso Importante

Las predicciones generadas por esta aplicación **no deben** ser consideradas como un diagnóstico médico.

Por favor, recuerde:

• Este modelo se entrenó con un conjunto de datos de muestra y tiene limitaciones.

• La predicción es generada por un algoritmo de aprendizaje automático y puede ser incorrecta.

• **Nunca** debe sustituir el consejo médico profesional.

• Consulte siempre a un psicólogo cualificado para obtener un diagnóstico, tratamiento y asesoramiento médico.
""")

st.info("""
### 🔒 Aviso de Privacidad

Esta aplicación está diseñada con fines de demostración.

- No se almacena intencionadamente información personal.
- Las entradas del usuario solo se utilizan para generar una predicción durante la sesión actual.
""")

st.success("""
### 🎯 Objetivo de este proyecto

El objetivo de este proyecto es demostrar un flujo de trabajo de aprendizaje automático (Machine Learning) de 
principio a fin, que incluye:

• Limpieza y preprocesamiento de datos

• Integración con bases de datos SQL

• Desarrollo de modelos de aprendizaje automático

• Evaluación del modelo

• Despliegue del modelo mediante Streamlit

Este proyecto sirve como elemento de portafolio para mostrar habilidades prácticas en ciencia de datos, análisis de datos, 
ingeniería de datos, aprendizaje automático y desarrollo de aplicaciones web.
""")

st.markdown("---")
st.caption(
    "© 2026 Sistema de Predicción de Nivel de Estrés | Proyecto Educativo y de Portafolio | "
    "Desarrollado para demostrar habilidades en Análisis de Datos y Aprendizaje Automático."
)