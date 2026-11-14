
import streamlit as st


def render_sidebar():
    """
    Renderiza la identidad visual del menú lateral.
    """

    with st.sidebar:

        st.title("Sala Situacional")

        st.caption("Sistema de información en salud")

        st.divider()

        st.markdown(
            """
            **Plataforma de análisis**

            Información epidemiológica
            """
        )

        st.divider()

