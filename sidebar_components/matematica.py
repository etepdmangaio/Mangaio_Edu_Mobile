import streamlit as st

def sidebar_matematica():
    with st.sidebar.expander("📐 Matemática", expanded=False):
        return st.selectbox("Escolha um tópico", [
            "Álgebra",
            "Geometria",
            "Probabilidade"
        ], key="matematica_topico")
