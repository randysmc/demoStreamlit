
import streamlit as st

from app.components.sidebar import render_sidebar



st.set_page_config(
    page_title="Sala Situacional de Salud",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configuración visual del sidebar
render_sidebar()


# Definición de las páginas
pages = {
    "Principal": [
        st.Page(
            "pages/dashboard.py",
            title="Dashboard",
            icon=":material/dashboard:",
            default=True
        )
    ],

    "Gestión de datos": [
        st.Page(
            "pages/data_upload.py",
            title="Carga de información",
            icon=":material/upload_file:"
        ),
        st.Page(
            "pages/data_management.py",
            title="Gestión de registros",
            icon=":material/database:"
        )
    ],

    "Análisis": [
        st.Page(
            "pages/reports.py",
            title="Reportes",
            icon=":material/analytics:"
        )
    ]
}


# Crear navegación
navigation = st.navigation(
    pages,
    position="sidebar"
)


# Ejecuta pagina seleccionada
navigation.run()
