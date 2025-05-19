import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def _dashboard_usuario():
  
    
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
        filtro = "Por usuário" # st.sidebar.radio("Filtrar resultados por:", ("Todos", "Por usuário"))

        if filtro == "Por usuário":
            usuario_selecionado =  st.selectbox("Escolha o usuário:", df["Usuário"])
            df = df[df["Usuário"] == usuario_selecionado]

        # Exibir gráfico
        st.title("📊 Desempenho dos Usuários no Quiz")
        st.bar_chart(df.set_index("Usuário"))
