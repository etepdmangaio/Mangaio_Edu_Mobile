import sys
import os
import streamlit as st
from login import pagina_login
from app import pagina_app

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    if "pagina" not in st.session_state:
        st.session_state["pagina"] = "login"

    if st.session_state["pagina"] == "login":
        pagina_login()
        
    elif st.session_state["pagina"] == "app":
        pagina_app()

if __name__ == "__main__":
    main()
        

    