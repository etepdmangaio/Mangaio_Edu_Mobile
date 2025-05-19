import streamlit as st
from sidebar_components.matematica.matematica import sidebar_matematica
from sidebar_components.geografia.geografia import sidebar_geografia
from sidebar_components.logica_programacao.logica import sidebar_logica_programacao
from sidebar_components.historia.historia_crise_primeiro_reinado import _crise_primeiro_reinado
from sidebar_components.historia.historia_deflagracao_revolta_1824 import _historia_deflagracao_revolta_1824
from sidebar_components.historia.historia_repressao_imperial import _historia_repressao_imperial
from sidebar_components.historia.historia_consequencias import _historia_consequencias
from sidebar_components.historia.historia_influencias_liberais_republicanas import _historia_influe_liber_republ
from sidebar_components.historia.historia_insatisfacao_nordeste import _insatisfacao_nordeste
from sidebar_components.dashboard.dashboard_todos import _dashboard_todos
from sidebar_components.dashboard.dashboard_usuario import _dashboard_usuario


def pagina_app():
    st.set_page_config(page_title="MangaioEdu", layout="wide")

    st.title("📚 Mangaio - "
                     "Uma Plataforma Educacional Colaborativa")
    st.success(f"Bem-vindo, {st.session_state.get('usuario', '')}!")

    if st.button("Logout"):
        st.session_state.clear()
        st.session_state["pagina"] = "login"
        st.rerun()

    with st.expander("📖 História", expanded=False):
        subtema_escolhido_historia = st.selectbox("Escolha uma trilha: ", (
            "Crise do Primeiro Reinado", "Insatisfação do Nordeste", "Influências Liberais e Republicanas",
            "Deflagração da Revolta (1824)", "Repressão Imperial", "Consequências"), key="subtema")
        
        if subtema_escolhido_historia == "Crise do Primeiro Reinado":
            #dash = " "
            _crise_primeiro_reinado()
            
        
        if subtema_escolhido_historia == "Insatisfação do Nordeste":
            #dash = " "
            _insatisfacao_nordeste()


        if subtema_escolhido_historia == "Influências Liberais e Republicanas":
            #dash = " "
            _historia_influe_liber_republ()


        if subtema_escolhido_historia == "Deflagração da Revolta (1824)":
            #dash = " "
            _historia_deflagracao_revolta_1824()


        if subtema_escolhido_historia == "Repressão Imperial":
            #dash = " "
            _historia_repressao_imperial()


        if subtema_escolhido_historia == "Consequências":
            #dash = " "
            _historia_consequencias()

        
    with st.expander("📖 Geografia", expanded=False):
        # st.markdown("### Subtemas")
        subtema_escolhido_geografia = st.selectbox("Selecione uma cor: ", ("Climas do Brasil",
            "Relevo", "Urbanização", "Cartografia"))
             
        sidebar_geografia()

    with st.expander("📖 Matemática", expanded=False):
        # st.markdown("### Subtemas")
        subtema_escolhido_matematica = st.selectbox("Selecione uma cor: ", ("Álgebra",
            "Geometria",
            "Probabilidade"))
        sidebar_matematica()

    with st.expander("📖 Lógica de Programação", expanded=False):
        # st.markdown("### Subtemas")
        subtema_escolhido_logica =st.selectbox("Selecione uma cor: ", ("O que é Lógica?",
            "Python",
            "Variáveis",
            "Estrutura de decisão",
            "Estrutura de controle"))
        sidebar_logica_programacao()

    with st.expander("📖 Dashboards", expanded=False):
        # st.markdown("### Subtemas")
       dash = st.selectbox("Selecione um Dashboard: ", ("Todos", "Usuario"))

       if dash == "Todos":
        _dashboard_todos()

       if dash == "Usuario":
        _dashboard_usuario()

 








    






    




