import pandas as pd
from pathlib import Path
from typing import BinaryIO, Union

def read_excel_file(file_path: str) -> pd.DataFrame:
    """
    Lee la hoja del excel.

    Args:
        file_path: Ruta del archivo Excel.

    Returns:
        DataFrame con los registros
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo: {path}"
        )

    dataframe = pd.read_excel(
        path,
        sheet_name="datos_epidemiologicos"
    )

    return dataframe


def read_excel_upload(file: Union[BinaryIO, bytes]) -> pd.DataFrame:
    """
    Lee la hoja de datos  desde un archivo subido

    Args:
        file: objeto con .read() 

    Returns:
        DataFrame con los registros .
    """
    dataframe = pd.read_excel(
        file,
        sheet_name="datos_epidemiologicos"
    )

    return dataframe