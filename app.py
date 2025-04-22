import streamlit as st
from sidebar_components.matematica import sidebar_matematica
from sidebar_components.geografia import sidebar_geografia
from sidebar_components.historia import sidebar_historia2
from sidebar_components.Informacoes import sidebar_informacoes


st.set_page_config(page_title="MangaioEdu", layout="wide")

st.sidebar.title("📚 Mangaio - Plataforma Educacional Colaborativa")


sidebar_historia2()

sidebar_matematica()

sidebar_geografia()

sidebar_informacoes()
