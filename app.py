
import sys
import os
import streamlit as st
from controllers.login_controller import LoginController
from views.principal import Principal


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    # Inicializa estado de sessão
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
        st.session_state["username"] = None
        st.session_state["role"] = None
        st.session_state["pagina"] = "login"  # Definir página inicial como login

    # Gerenciar navegação
    if st.session_state["pagina"] == "login":
        LoginController()
        if st.session_state["logged_in"]:
            st.session_state["pagina"] = "principal"
            st.rerun()

    elif st.session_state["pagina"] == "principal":
        Principal()


if __name__ == "__main__":
    main()