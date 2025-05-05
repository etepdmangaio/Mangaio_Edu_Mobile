import streamlit as st
import streamlit.components.v1 as components
from streamlit_sortables import sort_items
import pydeck as pdk


def _insatisfacao_nordeste():

    abas = st.tabs(["📖 Introdução", "👤 Personagens", "🧠 Quiz"])

    with abas[0]:
        st.header("Introdução")
        st.write("""
        As elites do Nordeste, especialmente em Pernambuco, estavam profundamente descontentes com a centralização do poder nas mãos de Dom Pedro I e sua Constituição outorgada (1824), que limitava a autonomia provincial. 
        Além disso, a região sofria com crise econômica pós-Independência, altos impostos e a percepção de que o governo imperial privilegiava o Sudeste. Esses fatores, somados à influência de ideais republicanos e liberais,
        criaram um clima de revolta
        """)

        st.title('Mapa do Nordeste')
        pontos = [
            {"nome": "Recife", "coords": [-34.877002, -8.047562]},
            {"nome": "Salvador", "coords": [-38.501637, -12.977749]},
            {"nome": "Fortaleza", "coords": [-38.526670, -3.731862]},
            {"nome": "Natal", "coords": [-35.200916, -5.779257]},
            {"nome": "João Pessoa", "coords": [-34.845012, -7.119495]}
        ]

        layer = pdk.Layer(
            "ScatterplotLayer",
            data=pontos,
            get_position="coords",
            get_color=[255, 0, 0, 200],
            get_radius=20000,
            pickable=True
        )

        view_state = pdk.ViewState(
            longitude=-38.0,
            latitude=-8.5,
            zoom=5,
            pitch=0
        )

        st.pydeck_chart(pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            tooltip={"text": "{nome}"}
        ))

    with abas[1]:
        st.header("Personagens Importantes")

        st.title("Frei Caneca")
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(
                'https://averdade.org.br/wp-content/uploads/2025/02/P12-_-Frei-Caneca-_-Roberto-Ploeg-1068x1378.jpg', width=150)
        with col2:
            st.subheader('Joaquim da Silva Rabelo')
            st.markdown("""
                **Idade:** 45 anos  
                **Carreira:** Escritor, clérico católico e político.   
                **Influência:** líder e mártir da Confederação do Equador.      
                **Funções:** Como jornalista, esteve à frente do Typhis Pernambucano.                 
            """)
    with abas[2]:
        st.header("Quiz Rápido: A Crise do Primeiro Reinado.")

        perguntas = [
            {
                "pergunta": "Quem foi uma das principais lideranças intelectuais da Confederação do Equador?",
                "alternativas": [
                    "José Bonifácio",
                    "Frei Caneca",
                    "Dom Pedro I"
                ],
                "correta": "Frei Caneca"
            },
            {
                "pergunta": "Qual foi a principal motivação para o início da Confederação do Equador em 1824?",
                "alternativas": [
                    "O descontentamento com a Constituição outorgada por Dom Pedro I",
                    "A luta contra a escravidão",
                    "A invasão das tropas portuguesas"
                ],
                "correta": "O descontentamento com a Constituição outorgada por Dom Pedro I"
            },
            {
                "pergunta": "Além de Pernambuco, qual outra província apoiou o movimento da Confederação do Equador?",
                "alternativas": [
                    "Minas Gerais",
                    "Ceará",
                    "São Paulo"
                ],
                "correta": "Ceará"
            },
            {
                "pergunta": "O que aconteceu com Frei Caneca após o fracasso da Confederação do Equador?",
                "alternativas": [
                    "Fugiu para Portugal",
                    "Foi executado por fuzilamento",
                    "Tornou-se conselheiro de Dom Pedro I"
                ],
                "correta": "Foi executado por fuzilamento"
            },
            {
                "pergunta": "Em qual cidade pernambucana se concentrou a maior resistência durante a Confederação do Equador?",
                "alternativas": [
                    "Recife",
                    "Olinda",
                    "Goiana"
                ],
                "correta": "Goiana"
            }
        ]

        acertos = 0
        erros = 0

        for i, p in enumerate(perguntas):
            st.subheader(f"{i+1}. {p['pergunta']}")
            resposta = st.radio(
                "Escolha uma alternativa:",
                options=p["alternativas"],
                key=f"resposta_deflagracao_revolta{i}"
            )

        # Verificação e contagem (fora do loop de exibição das perguntas)
        if st.button("Ver resultado"):
            for i, p in enumerate(perguntas):
                resposta = st.session_state.get(
                    f"resposta_deflagracao_revolta{i}")
                if resposta == p["correta"]:
                    acertos += 1
                else:
                    erros += 1

            st.markdown("---")
            st.success(f"✅ Total de acertos: **{acertos}**")
            st.error(f"❌ Total de erros: **{erros}**")
