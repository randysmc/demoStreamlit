import streamlit as st

from src.ingestion.excel_reader import read_excel_upload
from src.validation.data_validator import validate_dataframe


def main():

    st.title("Carga de información")
    st.caption("Importación de archivos epidemiológicos")
    st.divider()

    st.markdown(
        """
        Excel con formato correcto sobre los datos
        """
    )

    uploaded_file = st.file_uploader(
        "Selecciona un archivo Excel",
        type=["xlsx"],
    )

    if uploaded_file is None:
        st.info("Selecciona un archivo para continuar.")
        # limpiar datos
        # if "epidemiological_data" in st.session_state:
        #     del st.session_state["epidemiological_data"]
        #     del st.session_state["uploaded_file_name"]
        return

    st.success(f"Archivo recibido: **{uploaded_file.name}**")
    st.write(f"Tamaño: {uploaded_file.size:,} bytes")

    try:
        # 1. Leer
        dataframe = read_excel_upload(uploaded_file)

        # 2. Validar
        validation = validate_dataframe(dataframe)

        st.subheader("Resultado")
        st.json(validation)

        problemas = {
            k: v
            for k, v in validation.items()
            if k != "total_registros" and v != 0
        }

        if problemas:
            st.warning(
                "Hay observaciones de calidad. "
                "Revisa antes de usar el Dashboard."
            )
            st.write(problemas)
        else:
            st.success("Validaciones básicas correctas.")

        # 3. Vista previa
        st.subheader("Vista previa")
        st.dataframe(
            dataframe.head(20),
            use_container_width=True,
            hide_index=True,
        )
        st.caption(f"Total de filas leídas: {len(dataframe):,}")

        # 4. Confirmar uso en el Dashboard
        if st.button("Usar estos datos en el Dashboard", type="primary"):
            st.session_state["epidemiological_data"] = dataframe
            st.session_state["uploaded_file_name"] = uploaded_file.name
            st.success(
                "Datos cargados en la sesión. "
                
            )

    except ValueError as exc:
        # Hoja inexistente u otro error de Excel
        st.error(
            f"No se pudo leer el Excel. "
            f"¿Existe la hoja 'datos_epidemiologicos'? Detalle: {exc}"
        )
    except Exception as exc:
        st.error(f"Error al procesar el archivo: {exc}")


main()