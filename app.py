import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
df = pd.read_csv("vehicles_us.csv")

# Botón 1: Histograma
if st.button('Construir histograma'):
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón 2: Colores más vendidos
if st.button('Colores de Vehículos más vendidos'):
    st.write('Creación de reporte: colores de vehículos más vendidos')
    df_grouped_color = df['paint_color'].value_counts().reset_index()
    df_grouped_color.columns = ['paint_color', 'count']
    fig = px.bar(df_grouped_color, x="paint_color", y="count",
                 title="Autos vendidos por color",
                 labels={"paint_color": "Color", "count": "Número de Autos"},
                 color="count",
                 color_continuous_scale="Blues")
    fig.update_layout(xaxis={'categoryorder': 'total descending'})
    st.plotly_chart(fig, use_container_width=True)

# Botón 3: Modelos más vendidos
if st.button('Vehículos más vendidos'):
    st.write("Gráfica de modelos de vehículos más vendidos")

    # Agrupar por modelo y calcular precio medio (puedes cambiarlo a count si prefieres cantidad de ventas)
    df_grouped_model = df.groupby('model')['price'].mean().reset_index()
    df_grouped_model = df_grouped_model.sort_values(by="price", ascending=False)

    # Crear gráfico de barras horizontales
    fig = px.bar(df_grouped_model,
                 x="price",
                 y="model",
                 orientation='h',
                 title="Ventas por modelo de coche (precio medio)",
                 labels={"model": "Modelo", "price": "Precio medio (€)"},
                 color="price",
                 color_continuous_scale="Blues")
    
    st.plotly_chart(fig, use_container_width=True)