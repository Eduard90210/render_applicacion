import pandas as pd
import plotly.express as px
import streamlit as st
df = pd.read_csv("../vehicles_us.csv")
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(df, x="odometer")
        
     # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)