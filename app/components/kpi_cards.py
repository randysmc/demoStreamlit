
import streamlit as st


def render_kpi_cards(kpis: dict):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Total de casos",
            value=f'{kpis["total_casos"]:,}'
        )

    with col2:
        st.metric(
            label="Hospitalizados",
            value=f'{kpis["total_hospitalizados"]:,}'
        )

    with col3:
        st.metric(
            label="Fallecidos",
            value=f'{kpis["total_fallecidos"]:,}'
        )

    with col4:
        st.metric(
            label="Registros analizados",
            value=f'{kpis["total_registros"]:,}'
        )

    col5, col6 = st.columns(2)

    with col5:
        st.info(
            f'Enfermedad con más casos: '
            f'{kpis["enfermedad_principal"]}'
        )

    with col6:
        st.info(
            f'Departamento con más casos: '
            f'{kpis["departamento_principal"]}'
        )
