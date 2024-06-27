# Set up
import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Histograma y Dispersion en funcion de el kilometraje de un vehiculo')

# 

car_data = pd.read_csv("../data/vehicles_us.csv")  # leer los datos
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir dispersión')


## Plots
if build_histogram:
    st.write('Histograma de anuncios de venta de coches')

    # Crear histograma

    fig = px.histogram(car_data, x='odometer')

    # Mostrar grafico plotly interactivo

    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write( 'Dispersión para los datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x='odometer', y="price")

    st.plotly_chart(fig, use_container_width=True)