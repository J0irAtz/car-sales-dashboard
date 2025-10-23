# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------------------------
# 1. Función de Carga de Datos (Buena Práctica: Uso de caché)
# ----------------------------------------------------

# El decorador st.cache_data evita que el archivo se lea varias veces
@st.cache_data
def load_data(file_path):
    # Cargar el archivo CSV
    data = pd.read_csv(file_path)
    return data

# ----------------------------------------------------
# 2. Lógica Principal de la Aplicación
# ----------------------------------------------------

# Título de la aplicación (Paso 4 - Encabezado)
st.header('Análisis de Anuncios de Venta de Coches Usados')

# Cargar el dataset (llamar a la función)
# Asegúrate de que 'vehicles_us.csv' esté en la misma carpeta que 'app.py'
car_data = load_data('vehicles_us.csv')

# ----------------------------------------------------
# 3. Creación de Componentes Interactivos (Casillas de Verificación)
# ----------------------------------------------------

st.subheader('Creación de Gráficos')

# Crear las casillas de verificación (Desafío Extra - Mejor UI que solo botones)
build_histogram = st.checkbox('Construir un histograma de Odometer')
build_scatter = st.checkbox('Construir un gráfico de dispersión (Scatter)')

# ----------------------------------------------------
# 4. Lógica Condicional (Si la casilla está seleccionada)
# ----------------------------------------------------

# Lógica para el Histograma
if build_histogram:
    st.write('Creación de un histograma para la columna Odometer')

    # Crear el histograma con Plotly Express
    # Usamos la columna 'odometer' (kilometraje)
    fig_hist = px.histogram(
        car_data, 
        x="odometer", 
        title="Distribución de Kilometraje (Odometer)"
    )

    # Mostrar un gráfico Plotly interactivo en Streamlit
    st.plotly_chart(fig_hist, use_container_width=True)

# Lógica para el Gráfico de Dispersión
if build_scatter:
    st.write('Creación de un gráfico de dispersión (Price vs. Odometer)')

    # Crear el gráfico de dispersión con Plotly Express
    # Usamos las columnas 'odometer' y 'price'
    fig_scatter = px.scatter(
        car_data, 
        x="odometer", 
        y="price", 
        title="Precio vs. Kilometraje"
    )

    # Mostrar un gráfico Plotly interactivo en Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)