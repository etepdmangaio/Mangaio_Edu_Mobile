import streamlit as st
import streamlit.components.v1 as components
from streamlit_sortables import sort_items
import pandas as pd


def _dashboard_todos():

    # Tabs com conteúdos variados
    abas = st.tabs(["📖 Todos"])
    
    with abas[0]:
        dados_respostas = {
                "usuario1": {"corretas": 4, "erradas": 6},
                "usuario2": {"corretas": 3, "erradas": 7},
                "usuario3": {"corretas": 4, "erradas": 6},
                "usuario4": {"corretas": 2, "erradas": 8},
                "usuario5": {"corretas": 2, "erradas": 8},
                "usuario6": {"corretas": 3, "erradas": 7},
                "usuario7": {"corretas": 2, "erradas": 8},
                "usuario8": {"corretas": 3, "erradas": 7},
                "usuario9": {"corretas": 3, "erradas": 7},
                "usuario10": {"corretas": 2, "erradas": 8}
            }

            # Transformar em DataFrame
        df = pd.DataFrame.from_dict(dados_respostas, orient='index').reset_index()
        df.columns = ['Usuário', 'Corretas', 'Erradas']

            # Sidebar para seleção
        filtro = "Todos" # st.sidebar.radio("Filtrar resultados por:", ("Todos", "Por usuário"))

        if filtro == "Por usuário":
                usuario_selecionado = st.sidebar.selectbox("Escolha o usuário:", df["Usuário"])
                df = df[df["Usuário"] == usuario_selecionado]

            # Exibir gráfico
        st.title("📊 Desempenho dos Usuários no Quiz")
        st.bar_chart(df.set_index("Usuário"))
    

    
