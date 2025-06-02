import streamlit as st
from areaconhecimento.historia.historia_crise_primeiro_reinado import _crise_primeiro_reinado
from areaconhecimento.historia.historia_consequencias import _historia_consequencias
from areaconhecimento.historia.historia_insatisfacao_nordeste import _insatisfacao_nordeste
from areaconhecimento.historia.historia_deflagracao_revolta_1824 import _historia_deflagracao_revolta_1824
from areaconhecimento.historia.historia_influencias_liberais_republicanas import _historia_influe_liber_republ
from areaconhecimento.historia.historia_repressao_imperial import _historia_repressao_imperial
from models.database import Database

class Principal:
    def __init__(self):
        """Inicializa a página principal"""
        st.set_page_config(page_title="MangaioEdu", layout="wide")
        self.db=Database()
        self.exibir_pagina()


    def exibir_pagina(self):
        """Renderiza a interface principal"""

        st.title("📚 Mangaio - Uma Plataforma Educacional Colaborativa")
        st.success(f"Bem-vindo, {st.session_state.get('username', '')}!")
        username = st.session_state.get('username')
        #print('Usuario: ', username)

        if st.button("Logout"):
            st.session_state.clear()
            st.session_state["pagina"] = "login"
            st.rerun()

        self.exibir_historia()
        self.exibir_geografia()
        self.exibir_matematica()
        self.exibir_logica_programacao()
        self.exibir_dashboard()
        if username == "admin":
            #print('Usuario admin: ', username)
            self.exibir_cadastro_pergunta()

            

    def exibir_historia(self):
        """Cria o bloco de História"""
        with st.expander("📖 História", expanded=False):
            subtema_escolhido_historia = st.selectbox(
                "Escolha uma trilha:", [
                    "Crise do Primeiro Reinado",
                    "Insatisfação do Nordeste",
                    "Influências Liberais e Republicanas",
                    "Deflagração da Revolta (1824)",
                    "Repressão Imperial",
                    "Consequências"
                ],
                key="subtema"
            )

            if subtema_escolhido_historia == "Crise do Primeiro Reinado":
                _crise_primeiro_reinado(st.session_state.get('username'))

            elif subtema_escolhido_historia == "Insatisfação do Nordeste":
                _insatisfacao_nordeste(st.session_state.get('username'))

            elif subtema_escolhido_historia == "Influências Liberais e Republicanas":
                _historia_influe_liber_republ(st.session_state.get('username'))

            elif subtema_escolhido_historia == "Deflagração da Revolta (1824)":
                _historia_deflagracao_revolta_1824(st.session_state.get('username'))

            elif subtema_escolhido_historia == "Repressão Imperial":
                _historia_repressao_imperial(st.session_state.get('username'))

            elif subtema_escolhido_historia == "Consequências":
                _historia_consequencias(st.session_state.get('username'))
                

    def exibir_geografia(self):
        """Cria o bloco de Geografia"""
        with st.expander("📖 Geografia", expanded=False):
            sidebar_geografia = st.selectbox(
                "Selecione um tema:", [
                    "Climas do Brasil",
                    "Relevo",
                    "Urbanização",
                    "Cartografia"
                ]
            )

    def exibir_matematica(self):
        """Cria o bloco de Matematica"""
        with st.expander("📖 Matematica", expanded=False):
            sidebar_matematica = st.selectbox(
                "Selecione um tema:", [
                    "Álgebra",
                    "Geometria",
                    "Probabilidade"
                ]
            )

    def exibir_logica_programacao(self):
        """Cria o bloco de Lógica de Programação"""
        with st.expander("📖 Lógica de Programação", expanded=False):
            sidebar_logica_programacao = st.selectbox(
                "Selecione um tema:", [
                    "O que é Lógica?",
                    "Python",
                    "Variáveis",
                    "Estrutura de decisão",
                    "Estrutura de controle"
                ]
            )

    def exibir_dashboard(self):
        """Cria o bloco de DAshboard"""
        with st.expander("📖 Dashboard", expanded=False):
            sidebar_dashboard = st.selectbox(
                "Selecione um Dashboard:", [
                    "Todos", "Usuario"
                ]
            )

    def exibir_cadastro_pergunta(self):
        """Permite que administradores cadastrem novas perguntas"""
        with st.expander("Cadastrar Nova Questão 📌", expanded=False):
            area_conhecimento = st.selectbox("Área de Conhecimento", ["História", "Geografia"])
            categoria = st.selectbox("Categoria", ["Crise do Primeiro Reinado",
                        "Insatisfação do Nordeste",
                        "Influências Liberais e Republicanas",
                        "Deflagração da Revolta (1824)",
                        "Repressão Imperial",
                        "Consequências"] )
            pergunta = st.text_area("Digite a Pergunta")
            opcao1 = st.text_input("Opção 1")
            opcao2 = st.text_input("Opção 2")
            opcao3 = st.text_input("Opção 3")
            opcao4 = st.text_input("Opção 4")
            resposta_correta = st.selectbox("Resposta Correta", [opcao1, opcao2, opcao3, opcao4])

            if st.button("Cadastrar Questão"):
                sucesso = self.db.cadastrar_pergunta(area_conhecimento, categoria, pergunta, [opcao1, opcao2, opcao3, opcao4], resposta_correta)
                if sucesso:
                    st.success("Questão cadastrada com sucesso!")
                    
                else:
                    st.error("Erro ao cadastrar questão. Verifique os dados.")

