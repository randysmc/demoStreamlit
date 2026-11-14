
import pandas as pd


def calculate_kpis(dataframe: pd.DataFrame) -> dict:
    """
    Calcula los indicadores.
    """

    total_casos = dataframe["casos"].sum()

    total_hospitalizados = dataframe["hospitalizados"].sum()

    total_fallecidos = dataframe["fallecidos"].sum()

    total_registros = len(dataframe)

    enfermedad_principal = (
        dataframe.groupby("enfermedad")["casos"]
        .sum()
        .idxmax()
    )

    departamento_principal = (
        dataframe.groupby("departamento")["casos"]
        .sum()
        .idxmax()
    )

    return {
        "total_casos": int(total_casos),
        "total_hospitalizados": int(total_hospitalizados),
        "total_fallecidos": int(total_fallecidos),
        "total_registros": int(total_registros),
        "enfermedad_principal": enfermedad_principal,
        "departamento_principal": departamento_principal
    }
