from models.database import Database
from views.login_view import LoginView
from utils.validacao import email_valido  # importando validação
import streamlit as st

class LoginController:
    def __init__(self):
        self.db = Database()
        self.view = LoginView()
        self.processar_login()

    def processar_login(self):
        """Gerencia login e sessões"""
        if "logged_in" not in st.session_state:
            st.session_state.logged_in = False

        if st.session_state.logged_in:
            self.exibir_pagina_usuario()
        else:
            self.exibir_login()

    def exibir_login(self):
        """Tela de login"""
        if self.view.login_button:
            role = self.db.verificar_usuario(self.view.username, self.view.password)
            if role:
                st.session_state.logged_in = True
                st.session_state.username = self.view.username
                st.session_state.role = role
                st.success(f"Bem-vindo, {self.view.username}! (Acesso: {role})")
                st.rerun()
            else:
                st.error("Usuário ou senha incorretos.")

        if self.view.register_button:
            if not email_valido(self.view.email):
                st.error("E-mail inválido. Por favor, insira um e-mail válido.")
            elif self.db.cadastrar_usuario(self.view.username, self.view.email, self.view.password):
                st.success("Usuário cadastrado com sucesso! Agora faça login.")
            else:
                st.error("Usuário já existe ou erro no cadastro.")

    def exibir_pagina_usuario(self):
        """Exibe página pós-login com base na permissão"""
        if st.session_state.role == "admin":
            st.title(f"Bem-vindo, {st.session_state.username}! Você é um **Administrador** 🛠️")
            st.write("Aqui você pode gerenciar usuários, visualizar relatórios e configurar o sistema.")
        else:
            st.title(f"Bem-vindo, {st.session_state.username}!")
            st.write("Você tem acesso padrão ao sistema.")

        if st.button("Sair"):
            st.session_state.logged_in = False
            st.rerun()
