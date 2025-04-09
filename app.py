import pandas as pd
import plotly.express as px
import streamlit as st
df = pd.read_csv("vehicles_us.csv")

hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(df, x="odometer")
        
     # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


hist_button = st.button('Colores de Vahiculos mas vendidos') # crear un botón
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de reporte colores de vehiculos mas vendidos')
    fig = px.bar(df_grouped_color, x="paint_color", y="price",
             title="Autos Vendidos por color",
             labels={"paint_color": "Color", "price": "Num Autos"},
             color="price",
             color_continuous_scale="Blues")

# Ordenar por precio descendente (opcional)
fig.update_layout(xaxis={'categoryorder':'total descending'})

fig.show()