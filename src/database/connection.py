import os
from pathlib import Path

import oracledb
from dotenv import load_dotenv


# Ubicación del archivo .env en la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = BASE_DIR / ".env"

# Cargar variables de entorno
load_dotenv(ENV_FILE)


def get_connection():
    """
    Establece una conexión con Oracle Database.
    """

    user = os.getenv("ORACLE_USER")
    password = os.getenv("ORACLE_PASSWORD")
    dsn = os.getenv("ORACLE_DSN")

    # Validar configuración
    missing = [
        name
        for name, value in {
            "ORACLE_USER": user,
            "ORACLE_PASSWORD": password,
            "ORACLE_DSN": dsn,
        }.items()
        if not value
    ]

    if missing:
        raise ValueError(
            f"Faltan variables de configuración: {', '.join(missing)}"
        )

    # Crear conexión
    return oracledb.connect(
        user=user,
        password=password,
        dsn=dsn,
    )