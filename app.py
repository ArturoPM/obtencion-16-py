import streamlit as st

# Título de la app
st.title("Calculadora del 16%")

# Texto de apoyo
st.write("Ingresa un número y obtén el 16% de ese valor.")

# Entrada del usuario
numero = st.number_input("Escribe un número:", min_value=0.0, step=1.0)

# Botón para calcular
if st.button("Calcular"):
    resultado = numero * 0.16
    st.success(f"El 16% de {numero} es {resultado}")