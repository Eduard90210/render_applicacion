import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
df = pd.read_csv("vehicles_us.csv")

# Botón para el histograma
if st.button('Construir histograma'):
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para colores de vehículos más vendidos
if st.button('Colores de Vehículos más vendidos'):
    st.write('Creación de reporte: colores de vehículos más vendidos')

    # Agrupar por color de pintura y contar número de coches
    df_grouped_color = df['paint_color'].value_counts().reset_index()
    df_grouped_color.columns = ['paint_color', 'count']

    # Crear gráfico de barras
    fig = px.bar(df_grouped_color, x="paint_color", y="count",
                 title="Autos vendidos por color",
                 labels={"paint_color": "Color", "count": "Número de Autos"},
                 color="count",
                 color_continuous_scale="Blues")

    # Ordenar por total descendente
    fig.update_layout(xaxis={'categoryorder': 'total descending'})

    st.plotly_chart(fig, use_container_width=True)