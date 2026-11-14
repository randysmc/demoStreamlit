"""
Componentes visuales de gráficos (Plotly + Streamlit).
No hace groupby ni cálculos de negocio.
"""

import streamlit as st
import plotly.express as px
import pandas as pd


def render_cases_by_disease_chart(df: pd.DataFrame) -> None:
    """Gráfico de barras: casos por enfermedad."""
    st.subheader("Casos por enfermedad")

    if df.empty:
        st.warning("No hay datos para graficar con los filtros actuales.")
        return

    fig = px.bar(
        df,
        x="enfermedad",
        y="casos",
        text="casos",
        labels={"enfermedad": "Enfermedad", "casos": "Casos"},
        title="Total de casos por enfermedad",
    )
    fig.update_traces(textposition="outside")
    #fig.update_layout(xaxis_tickangle=-25)

    st.plotly_chart(fig, use_container_width=True)


def render_cases_by_department_chart(df: pd.DataFrame) -> None:
    """Gráfico de barras: casos por departamento."""
    st.subheader("Casos por departamento")

    if df.empty:
        st.warning("No hay datos para graficar con los filtros actuales.")
        return

    fig = px.bar(
        df,
        x="departamento",
        y="casos",
        text="casos",
        labels={"departamento": "Departamento", "casos": "Casos"},
        title="Total de casos por departamento",
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(xaxis_tickangle=-30)

    st.plotly_chart(fig, use_container_width=True)


def render_cases_by_month_chart(df: pd.DataFrame) -> None:
    """Gráfico de línea: tendencia de casos por mes/año."""
    st.subheader("Tendencia de casos por mes")

    if df.empty:
        st.warning("No hay datos para graficar con los filtros actuales.")
        return

    fig = px.line(
        df,
        x="periodo",
        y="casos",
        markers=True,
        labels={"periodo": "Período", "casos": "Casos"},
        title="Evolución temporal de casos",
    )
    fig.update_layout(xaxis_tickangle=-45)

    st.plotly_chart(fig, use_container_width=True)