import streamlit as st
import pandas as pd

# Título
st.title("Calculadora de interés compuesto")

st.write(
    "Simula una inversión con interés compuesto diario. "
    "Los primeros $25,000 generan 13% anual y el resto 7% anual."
)

# Inputs
cantidad_inicial = st.number_input("Cantidad inicial", min_value=0.0, step=100.0)
cantidad_mensual = st.number_input("Cantidad ingresada mensualmente", min_value=0.0, step=100.0)
anios = st.number_input("Cantidad de años", min_value=1, step=1)

# Botón
if st.button("Calcular"):

    dias_totales = int(anios * 365)

    balance = cantidad_inicial
    datos = []

    inicio_anio = balance
    rendimiento_anio = 0

    for dia in range(1, dias_totales + 1):

        # ingreso mensual cada 30 días
        if dia % 30 == 0:
            balance += cantidad_mensual

        # división de tramos de interés
        parte_13 = min(balance, 25000)
        parte_7 = max(balance - 25000, 0)

        interes_dia = (parte_13 * (0.13 / 365)) + (parte_7 * (0.07 / 365))

        balance += interes_dia
        rendimiento_anio += interes_dia

        # cierre de año
        if dia % 365 == 0:

            datos.append({
                "Año": int(dia / 365),
                "Dinero inicial del año": inicio_anio,
                "Rendimiento generado": rendimiento_anio,
                "Total del año": balance
            })

            inicio_anio = balance
            rendimiento_anio = 0

    df = pd.DataFrame(datos)

    # Formato con separador de miles
    df["Dinero inicial del año"] = df["Dinero inicial del año"].map("${:,.2f}".format)
    df["Rendimiento generado"] = df["Rendimiento generado"].map("${:,.2f}".format)
    df["Total del año"] = df["Total del año"].map("${:,.2f}".format)

    st.subheader("Resultado por año")
    st.dataframe(df)

    st.success(f"Total final después de {anios} años: ${balance:,.2f}")