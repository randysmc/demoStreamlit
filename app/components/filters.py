import streamlit as st


def render_filters(dataframe):

    st.subheader("Filtros de consulta")

    col1, col2, col3 = st.columns(3)

    with col1:
        anios = sorted(dataframe["anio"].unique())
        anio = st.selectbox(
            "Año",
            options=["Todos"] + list(anios),
        )

    with col2:
        meses = sorted(dataframe["mes"].unique())
        mes = st.selectbox(
            "Mes",
            options=["Todos"] + list(meses),
            format_func=lambda x: (
                "Todos"
                if x == "Todos"
                else dataframe.loc[
                    dataframe["mes"] == x, "nombre_mes"
                ].iloc[0]
            ),
        )

    with col3:
        departamentos = sorted(dataframe["departamento"].unique())
        departamento = st.selectbox(
            "Departamento",
            options=["Todos"] + list(departamentos),
        )

    col4, col5, col6 = st.columns(3)

    with col4:
        municipios = sorted(dataframe["municipio"].unique())
        municipio = st.selectbox(
            "Municipio",
            options=["Todos"] + list(municipios),
        )

    with col5:
        enfermedades = sorted(dataframe["enfermedad"].unique())
        enfermedad = st.selectbox(
            "Enfermedad",
            options=["Todas"] + list(enfermedades),
        )

    with col6:
        sexos = sorted(dataframe["sexo"].unique())
        sexo = st.selectbox(
            "Sexo",
            options=["Todos"] + list(sexos),
        )

    # Nueva fila: grupo de edad
    col7, _, _ = st.columns(3)

    with col7:
        grupos_edad = sorted(dataframe["grupo_edad"].unique())
        grupo_edad = st.selectbox(
            "Grupo de edad",
            options=["Todos"] + list(grupos_edad),
        )

    return {
        "anio": None if anio == "Todos" else anio,
        "mes": None if mes == "Todos" else mes,
        "departamento": None if departamento == "Todos" else departamento,
        "municipio": None if municipio == "Todos" else municipio,
        "enfermedad": None if enfermedad == "Todas" else enfermedad,
        "sexo": None if sexo == "Todos" else sexo,
        "grupo_edad": None if grupo_edad == "Todos" else grupo_edad,
    }