
import pandas as pd


def cases_by_disease(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula el total de casos por enfermedad.
    """

    result = (
        dataframe
        .groupby("enfermedad")
        .agg(
            total_casos=("casos", "sum"),
            total_registros=("id_registro", "count"),
            total_hospitalizados=("hospitalizados", "sum"),
            total_fallecidos=("fallecidos", "sum")
        )
        .reset_index()
        .sort_values(
            by="total_casos",
            ascending=False
        )
    )

    return result


def cases_by_department(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula el total de casos por departamento.
    """

    result = (
        dataframe
        .groupby("departamento")
        .agg(
            total_casos=("casos", "sum"),
            total_registros=("id_registro", "count")
        )
        .reset_index()
        .sort_values(
            by="total_casos",
            ascending=False
        )
    )

    return result


def cases_by_month(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula el total de casos por año y mes.
    """

    result = (
        dataframe
        .groupby(["anio", "mes", "nombre_mes"])
        .agg(
            total_casos=("casos", "sum")
        )
        .reset_index()
        .sort_values(
            by=["anio", "mes"]
        )
    )

    return result


def cases_by_age_group(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula el total de casos por grupo de edad.
    """

    result = (
        dataframe
        .groupby("grupo_edad")
        .agg(
            total_casos=("casos", "sum")
        )
        .reset_index()
        .sort_values(
            by="total_casos",
            ascending=False
        )
    )

    return result


def cases_by_sex(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula el total de casos por sexo.
    """

    result = (
        dataframe
        .groupby("sexo")
        .agg(
            total_casos=("casos", "sum")
        )
        .reset_index()
        .sort_values(
            by="total_casos",
            ascending=False
        )
    )

    return result
