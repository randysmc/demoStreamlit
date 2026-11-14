
import pandas as pd


def validate_dataframe(dataframe: pd.DataFrame) -> dict:
    """
    Ejecuta validaciones.

    Args:
        dataframe: DataFrame con los registros.

    Returns:
        Diccionario con los resultados de validación.
    """

    results = {}

    # Cantidad de registros
    results["total_registros"] = len(dataframe)

    # Identificadores duplicados
    results["ids_duplicados"] = int(
        dataframe["id_registro"].duplicated().sum()
    )

    # Valores nulos
    results["valores_nulos"] = int(
        dataframe.isnull().sum().sum()
    )

    # Casos negativos
    results["casos_negativos"] = int(
        (dataframe["casos"] < 0).sum()
    )

    # Hospitalizados superiores a casos
    results["hospitalizados_invalidos"] = int(
        (dataframe["hospitalizados"] > dataframe["casos"]).sum()
    )

    # Fallecidos superiores a casos
    results["fallecidos_invalidos"] = int(
        (dataframe["fallecidos"] > dataframe["casos"]).sum()
    )

    # Recuperados superiores a casos
    results["recuperados_invalidos"] = int(
        (dataframe["recuperados"] > dataframe["casos"]).sum()
    )

    # Año incorrecto
    results["anios_inconsistentes"] = int(
        (
            dataframe["anio"]
            != dataframe["fecha_reporte"].dt.year
        ).sum()
    )

    # Mes incorrecto
    results["meses_inconsistentes"] = int(
        (
            dataframe["mes"]
            != dataframe["fecha_reporte"].dt.month
        ).sum()
    )

    return results
