
import pandas as pd


def filter_dataframe(
    dataframe: pd.DataFrame,
    anio=None,
    mes=None,
    departamento=None,
    municipio=None,
    enfermedad=None,
    sexo=None,
    grupo_edad=None
) -> pd.DataFrame:
    """
    Filtra los registros segun los parámetros seleccionados.
    """

    filtered_data = dataframe.copy()

    if anio:
        filtered_data = filtered_data[
            filtered_data["anio"] == anio
        ]

    if mes:
        filtered_data = filtered_data[
            filtered_data["mes"] == mes
        ]

    if departamento:
        filtered_data = filtered_data[
            filtered_data["departamento"] == departamento
        ]

    if municipio:
        filtered_data = filtered_data[
            filtered_data["municipio"] == municipio
        ]

    if enfermedad:
        filtered_data = filtered_data[
            filtered_data["enfermedad"] == enfermedad
        ]

    if sexo:
        filtered_data = filtered_data[
            filtered_data["sexo"] == sexo
        ]

    if grupo_edad:
        filtered_data = filtered_data[
            filtered_data["grupo_edad"] == grupo_edad
        ]

    return filtered_data
