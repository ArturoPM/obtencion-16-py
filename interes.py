import streamlit as st
import pandas as pd

st.title("Calculadora de interés compuesto")

st.write(
    "Simulación con interés compuesto diario.\n"
    "Primeros $25,000 generan 13% anual y el resto 7% anual."
)

# Inputs
cantidad_inicial = st.number_input("Cantidad inicial", min_value=0.0, step=100.0)
cantidad_mensual = st.number_input("Cantidad ingresada mensualmente", min_value=0.0, step=100.0)
anios = st.number_input("Cantidad de años", min_value=1, step=1)

if st.button("Calcular"):

    dias_totales = int(anios * 365)

    balance = cantidad_inicial
    datos = []

    inicio_anio = balance
    rendimiento_anio_total = 0
    rendimiento_anio_13 = 0
    rendimiento_anio_7 = 0

    for dia in range(1, dias_totales + 1):

        # depósito mensual cada 30 días
        if dia % 30 == 0:
            balance += cantidad_mensual

        # dividir balance en tramos
        parte_13 = min(balance, 25000)
        parte_7 = max(balance - 25000, 0)

        interes_13 = parte_13 * (0.13 / 365)
        interes_7 = parte_7 * (0.07 / 365)

        interes_total = interes_13 + interes_7

        balance += interes_total

        rendimiento_anio_total += interes_total
        rendimiento_anio_13 += interes_13
        rendimiento_anio_7 += interes_7

        # cierre de año
        if dia % 365 == 0:

            datos.append({
                "Año": int(dia / 365),
                "Dinero inicial del año": inicio_anio,
                "Rendimiento 13%": rendimiento_anio_13,
                "Rendimiento 7%": rendimiento_anio_7,
                "Rendimiento generado": rendimiento_anio_total,
                "Total del año": balance
            })

            inicio_anio = balance
            rendimiento_anio_total = 0
            rendimiento_anio_13 = 0
            rendimiento_anio_7 = 0

    df = pd.DataFrame(datos)

    # formato dinero
    columnas_dinero = [
        "Dinero inicial del año",
        "Rendimiento 13%",
        "Rendimiento 7%",
        "Rendimiento generado",
        "Total del año"
    ]

    for col in columnas_dinero:
        df[col] = df[col].map("${:,.2f}".format)

    st.subheader("Resultado por año")
    st.dataframe(df)

    st.success(f"Total final después de {anios} años: ${balance:,.2f}")