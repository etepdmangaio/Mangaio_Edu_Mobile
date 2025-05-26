import streamlit as st

def verificar_login(usuario, senha):
    usuarios = {
        "admin": "123",
        "usuario": "123",
        
    }
    return usuario in usuarios and usuarios[usuario] == senha

def pagina_login():
    st.title(" 📖 MangaioEdu")

    with st.form("form_login"):
        usuario = st.text_input("Usuário").strip()
        senha = st.text_input("Senha", type="password").strip()
        login_button = st.form_submit_button("Login")

    if login_button:
        if verificar_login(usuario, senha):
            st.session_state["logado"] = True
            st.session_state["usuario"] = usuario
            st.session_state["pagina"] = "app"
            st.rerun()
            #st.success("Login realizado com sucesso!")
        else:
            st.error("Usuário ou senha incorretos.")

