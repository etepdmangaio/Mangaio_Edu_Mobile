import streamlit as st

class LoginView:
    def __init__(self):
        st.title(" 📖 MangaioEdu - Login")
        self.username = st.text_input("Usuário")
        self.email = st.text_input("E-mail").strip()
        self.password = st.text_input("Senha", type="password")
        self.login_button = st.button("Entrar")
        self.register_button = st.button("Registrar novo usuário")