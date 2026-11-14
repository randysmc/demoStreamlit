"""
Preparación de df para gráficos epidemiológicos.
"""

import pandas as pd


def prepare_cases_by_disease(df: pd.DataFrame) -> pd.DataFrame:
    """Total de casos por enfermedad."""
    if df.empty:
        return pd.DataFrame(columns=["enfermedad", "casos"])

    return (
        df.groupby("enfermedad", as_index=False)["casos"]
        .sum()
        .sort_values("casos", ascending=False)
        .reset_index(drop=True)
    )


def prepare_cases_by_department(df: pd.DataFrame) -> pd.DataFrame:
    """Total de casos por departamento."""
    if df.empty:
        return pd.DataFrame(columns=["departamento", "casos"])

    return (
        df.groupby("departamento", as_index=False)["casos"]
        .sum()
        .sort_values("casos", ascending=False)
        .reset_index(drop=True)
    )


def prepare_cases_by_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tendencia temporal: casos por año y mes.
    """
    if df.empty:
        return pd.DataFrame(
            columns=["anio", "mes", "nombre_mes", "periodo", "casos"]
        )

    result = (
        df.groupby(["anio", "mes", "nombre_mes"], as_index=False)["casos"]
        .sum()
        .sort_values(["anio", "mes"])
        .reset_index(drop=True)
    )

    result["periodo"] = (
        result["anio"].astype(str)
        + "-"
        + result["mes"].astype(str).str.zfill(2)
    )

    return result


def prepare_summary_by_disease(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tabla resumen para mostrar bajo los gráficos.
    Casos, hospitalizados, fallecidos y registros por enfermedad.
    """
    if df.empty:
        return pd.DataFrame(
            columns=[
                "enfermedad",
                "casos",
                "hospitalizados",
                "fallecidos",
                "registros",
            ]
        )

    return (
        df.groupby("enfermedad", as_index=False)
        .agg(
            casos=("casos", "sum"),
            hospitalizados=("hospitalizados", "sum"),
            fallecidos=("fallecidos", "sum"),
            registros=("id_registro", "count"),
        )
        .sort_values("casos", ascending=False)
        .reset_index(drop=True)
    )