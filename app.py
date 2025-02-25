import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el conjunto de datos
car_data = pd.read_csv('vehicles_us.csv', delimiter = ';')  # Reemplaza con la ruta correcta

# Encabezado
st.header("Análisis de datos con Streamlit y Plotly")

# Botón para generar el histograma
if st.button("Mostrar histograma"):
    fig = px.histogram(car_data, x="odometer")  # Reemplaza con el nombre correcto de la columna
    st.write("Histograma del Kilometraje de los vehículos")
    st.plotly_chart(fig)
    
if st.button("Mostrar Gráfico de Dispersión"):
    fig_scatter = px.scatter(car_data, x="odometer", y="price")  # Cambia columnas según tu análisis
    st.write("Gráfico de dispersión: Kilometraje vs Precio")
    st.plotly_chart(fig_scatter)