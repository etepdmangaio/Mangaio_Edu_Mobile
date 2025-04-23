import streamlit as st
from sidebar_components.matematica import sidebar_matematica
from sidebar_components.geografia import sidebar_geografia
from sidebar_components.historia import sidebar_historia2
from sidebar_components.historia import sidebar_historia3
# from sidebar_components.Informacoes import sidebar_informacoes


st.set_page_config(page_title="MangaioEdu", layout="wide")

st.sidebar.title("📚 Mangaio - Uma Plataforma Educacional Colaborativa")

with st.sidebar.expander("História", expanded=False):
    st.markdown("### Subtemas")
    subtema_escolhido = st.radio("Escolha um subtema", [
        "Crise do Primeiro Reinado", "Insatisfação do Nordeste", "Influências Liberais e Republicanas",
        "Deflagração da Revolta (1824)"], key="subtema")
st.write("Subtema selecionado:", subtema_escolhido)

if subtema_escolhido == "Crise do Primeiro Reinado":
    sidebar_historia2()
elif subtema_escolhido == "Insatisfação do Nordeste":
    sidebar_historia3()


sidebar_geografia()

sidebar_matematica()

# topico_matematica = sidebar_matematica()

# st.write("Tópico de matemática: ", topico_matematica)

# sidebar_informacoes()
