import pandas as pd 
import plotly.express as px
import streamlit as st

# Encabezado de la aplicación
st.header('EDA_CARS')

# Leer los datos
car_data = pd.read_csv('https://raw.githubusercontent.com/MarcosAcostaFernandez/Sprint6_Marcos/main/vehicles_us.csv')




# Crear una casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')

# Si la casilla de verificación está seleccionada
if build_histogram: 
    st.write('Construir un histograma para la columna odómetro')
    
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer", title="Histograma de Odómetro")
    
    # Mostrar un gráfico Plotly interactivo en Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón para el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

# Comprobar si el botón fue presionado
if scatter_button:
    st.write('Creación de un gráfico de dispersión de precio vs. kilometraje')
    
    # Crear el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Precio vs. Kilometraje")
    
    # Mostrar el gráfico Plotly interactivo en Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)
