from models.database import Database
from views.quiz_view import QuizView
import streamlit as st

class QuizController:
    def __init__(self, usuario_id):
        self.db = Database()
        self.usuario_id = usuario_id
        self.selecionar_categoria()

    def selecionar_categoria(self):
        """Usuário escolhe a área de conhecimento antes do quiz"""
        st.title("Escolha uma área de conhecimento")

        # Definição correta das áreas e categorias
        area_conhecimento  = st.selectbox("Área:", ["História", "Geografia"])

        categorias = {
            "História": [ 
                "Crise do Primeiro Reinado", "Insatisfação do Nordeste", 
                "Influências Liberais e Republicanas", "Deflagração da Revolta (1824)", 
                "Repressão Imperial", "Consequências"
            ],
            "Geografia": [
                "Climas do Brasil", "Relevo", "Urbanização", "Cartografia"
            ]
        }

        # Agora "area_conhecimento" sempre será válido no dicionário
        categoria = st.selectbox("Categoria:", categorias[area_conhecimento])

        if st.button("Iniciar Quiz"):
            self.exibir_quiz(area_conhecimento, categoria)

    def exibir_quiz(self, area_conhecimento, categoria):
        """Mostra as questões do quiz filtradas pela escolha do usuário"""
        perguntas = self.db.obter_questoes_por_categoria(area_conhecimento , categoria)
        if not perguntas:
            st.warning("Nenhuma pergunta cadastrada para essa área e categoria.")
            return
        
        print(perguntas[0])
        print("Teste")
        #self.view = QuizView(perguntas)
        if perguntas:
            primeira_pergunta = perguntas[0]  # Seleciona apenas a primeira pergunta
            self.view = QuizView(primeira_pergunta)
        else:
            st.warning("Nenhuma questão encontrada para essa categoria.")

        respostas = self.view.exibir_perguntas()

        if self.view.botao_confirmar_respostas():
            for quiz_id, resposta in respostas.items():
                self.db.registrar_resposta(self.usuario_id, quiz_id, resposta)
            st.success("Respostas enviadas com sucesso!")

    def cadastrar_respostas(self, quiz_id, resposta):
        self.db.registrar_resposta(self.usuario_id, quiz_id, resposta)
                #st.success("Respostas enviadas com sucesso!")