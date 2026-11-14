from src.database.connection import get_connection


def main():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT
                        SYS_CONTEXT('USERENV', 'DB_NAME'),
                        SYS_CONTEXT('USERENV', 'CON_NAME'),
                        USER
                    FROM dual
                """)

                resultado = cursor.fetchone()

                print("Conexión exitosa")
                print(f"Base de datos: {resultado[0]}")
                print(f"Contenedor: {resultado[1]}")
                print(f"Usuario: {resultado[2]}")

    except Exception as error:
        print(f"Error de conexión: {error}")


if __name__ == "__main__":
    main()