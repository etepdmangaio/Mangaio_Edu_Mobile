import streamlit as st

class QuizView:
    def __init__(self, pergunta):
        """Recebe uma única pergunta e exibe no layout"""
        st.title("Quiz Interativo")

        if pergunta:
            self.exibir_pergunta(pergunta)
        else:
            st.warning("Nenhuma pergunta encontrada para esta categoria.")

    def exibir_pergunta(self, pergunta):
        """Exibe uma única questão com suas opções"""
          # Texto da Pergunta
        st.subheader(pergunta[2])
        # Criando o botão de múltipla escolha com as alternativas

        if "respostas" not in st.session_state:
            st.session_state["respostas"] = {}

        resposta = st.radio(
            "Escolha uma resposta:",
            [pergunta[3], pergunta[4], pergunta[5], pergunta[6]],  # Pegando opções do banco
            key=f"questao_{pergunta[0]}"  # Identificador único
        )

        # Salvar resposta no estado da sessão
        if resposta:
            st.session_state["respostas"][pergunta[0]] =resposta

        if st.button("Enviar Resposta"):
            st.success("Resposta enviada com sucesso!")