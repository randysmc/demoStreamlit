import streamlit as st

# from src.ingestion.excel_reader import read_excel_file  # demo fijo (desactivado)
from src.analytics.kpi_analysis import calculate_kpis
from src.analytics.filters import filter_dataframe
from src.analytics.chart_analysis import (
    prepare_cases_by_disease,
    prepare_cases_by_department,
    prepare_cases_by_month,
    prepare_summary_by_disease,
)

from app.components.kpi_cards import render_kpi_cards
from app.components.filters import render_filters
from app.components.charts import (
    render_cases_by_disease_chart,
    render_cases_by_department_chart,
    render_cases_by_month_chart,
)


def main():

    st.title("Sala Situacional de Salud")
    st.caption("Panel de indicadores epidemiológicos")
    st.divider()


    # 1. Origen de datos: sesión (archivo subido)
    #    Demo fijo en disco — dejado comentado a propósito

    # dataframe = read_excel_file(
    #     "storage/raw/sala_situacional_demo.xlsx"
    # )

    if "epidemiological_data" not in st.session_state:
        st.warning(
            "No hay datos cargados "

        )
        st.stop()

    dataframe = st.session_state["epidemiological_data"]
    file_name = st.session_state.get("uploaded_file_name", "sesión actual")

    st.info(f"Analizando archivo: **{file_name}**")

    # 2. Filtros
    selected_filters = render_filters(dataframe)
    st.divider()

    # 3. Aplicar filtros
    filtered_data = filter_dataframe(
        dataframe,
        **selected_filters,
    )

    # 4. KPI
    kpis = calculate_kpis(filtered_data)
    st.subheader("Indicadores generales")
    render_kpi_cards(kpis)

    st.caption(f"Registros encontrados: {len(filtered_data):,}")
    st.divider()

    # 5. Datos para gráficos
    df_disease = prepare_cases_by_disease(filtered_data)
    df_department = prepare_cases_by_department(filtered_data)
    df_month = prepare_cases_by_month(filtered_data)
    df_summary = prepare_summary_by_disease(filtered_data)

    # 6. Gráficos
    st.subheader("Visualizaciones")

    col_a, col_b = st.columns(2)

    with col_a:
        render_cases_by_disease_chart(df_disease)

    with col_b:
        render_cases_by_department_chart(df_department)

    render_cases_by_month_chart(df_month)

    st.divider()

    # 7. Tabla resumen
    st.subheader("Tabla resumen por enfermedad")
    st.caption(
        "Totales según los filtros seleccionados "
        "(análisis descriptivo)."
    )

    if df_summary.empty:
        st.warning("No hay filas para mostrar en la tabla resumen.")
    else:
        st.dataframe(
            df_summary,
            use_container_width=True,
            hide_index=True,
        )


main()