import streamlit as st
import streamlit.components.v1 as components


def sidebar_historia2():
    # with st.sidebar.expander("História", expanded=False):
    #     st.markdown("### Subtemas")
    #     st.radio("Escolha um subtema", [
    #              "Crise do Primeiro Reinado", "Insatisfação do Nordeste "], key="subtema")

    # Tabs com conteúdos variados
    abas = st.tabs(["📖 Introdução", "🕒 Linha do Tempo",
                   "👤 Personagens", "Caça Palavras", "🧠 Quiz"])

    with abas[0]:
        st.header("Introdução")
        st.write("""
        A Crise do Primeiro Reinado (1822–1831) foi marcada por instabilidade política, econômica e social.
        A Confederação do Equador surge como uma reação ao autoritarismo de D. Pedro I.
        """)
        st.video("https://www.youtube.com/watch?v=_n6mLwFB1ss")
    with abas[1]:
        st.header("Linha do Tempo")
        st.markdown("""
        - **1822**: Independência do Brasil  
        - **1824**: Constituição outorgada  
        - **1824**: Eclosão da Confederação do Equador  
        - **1825**: Repressão e execução de líderes
        """)

    with abas[2]:
        st.header("Personagens Importantes")
        st.write("""
        - **Frei Caneca** – líder intelectual e político.
        - **Dom Pedro I** – Imperador autoritário que centralizou o poder.
        """)

    with abas[3]:

        st.header("Caça-palavras")
        st.write("🎮 Aqui é onde o jogo vai!")
        html_code = """
        <style>
        table {
            border-collapse: collapse;
            margin-bottom: 10px;
        }
        td {
            border: 1px solid black;
            padding: 10px;
            text-align: center;
            font-weight: bold;
            cursor: pointer;
            user-select: none;
        }
        td.selected {
            background-color: yellow;
        }
        td.found {
            background-color: lightgreen;
        }
        </style>

        <div id="game"></div>
        <button onclick="checkWord()">Verificar</button>
        <p id="status"></p>
        <p><b>Palavras para encontrar:</b> <span id="word-list"></span></p>

        <script>
        const words = ["PYTHON", "STREAMLIT", "JAVASCRIPT", "DATA"];
        let foundWords = [];
        let selectedCells = [];

        const grid = [
            ["S", "T", "R", "E", "A", "M", "L", "I", "T"],
            ["P", "Y", "T", "H", "O", "N", "D", "A", "A"],
            ["J", "A", "V", "A", "S", "C", "R", "T", "P"],
            ["T", "R", "U", "E", "E", "U", "A", "G", "X"],
            ["B", "U", "G", "L", "Z", "D", "Q", "P", "K"]
        ];

        function renderGrid() {
            let html = "<table>";
            for (let i = 0; i < grid.length; i++) {
            html += "<tr>";
            for (let j = 0; j < grid[i].length; j++) {
                html += `<td onclick="selectCell(this, ${i}, ${j})" data-i="${i}" data-j="${j}">${grid[i][j]}</td>`;
            }
            html += "</tr>";
            }
            html += "</table>";
            document.getElementById("game").innerHTML = html;
            document.getElementById("word-list").textContent = words.join(", ");
        }

        function selectCell(cell, i, j) {
            if (cell.classList.contains("found")) return;

            if (cell.classList.contains("selected")) {
            cell.classList.remove("selected");
            selectedCells = selectedCells.filter(c => !(c.i === i && c.j === j));
            } else {
            cell.classList.add("selected");
            selectedCells.push({ i, j, letter: grid[i][j], cell });
            }
        }

        function checkWord() {
            const formedWord = selectedCells.map(c => c.letter).join("");
            const upperWord = formedWord.toUpperCase();
            const status = document.getElementById("status");

            if (words.includes(upperWord) && !foundWords.includes(upperWord)) {
            selectedCells.forEach(c => c.cell.classList.add("found"));
            foundWords.push(upperWord);
            status.textContent = `✅ Palavra encontrada: ${upperWord}`;
            } else {
            status.textContent = `❌ Palavra inválida: ${upperWord}`;
            }

            selectedCells.forEach(c => c.cell.classList.remove("selected"));
            selectedCells = [];
        }

        renderGrid();
        </script>
        """
        components.html(html_code, height=450)

    with abas[4]:
        st.header("Quiz Rápido")
        pergunta = st.radio("O que foi a Confederação do Equador?", [
            "Movimento separatista em São Paulo",
            "Revolta contra o autoritarismo no Nordeste",
            "Conflito entre Portugal e Brasil"
        ])

        if pergunta:
            if pergunta == "Revolta contra o autoritarismo no Nordeste":
                st.success("✅ Resposta correta!")
            else:
                st.error("❌ Resposta incorreta.")

def sidebar_historia3():

    abas = st.tabs(["📖 Introdução","👤 Personagens", "🧠 Quiz"])

    with abas[0]:
        st.header("Introdução")
        st.write("""
        As elites do Nordeste, especialmente em Pernambuco, estavam profundamente descontentes com a centralização do poder nas mãos de Dom Pedro I e sua Constituição outorgada (1824), que limitava a autonomia provincial. 
        Além disso, a região sofria com crise econômica pós-Independência, altos impostos e a percepção de que o governo imperial privilegiava o Sudeste. Esses fatores, somados à influência de ideais republicanos e liberais,
        criaram um clima de revolta
        """)
        st.image("https://www.personacursos.com.br/pm/wp-content/uploads/2018/05/confederação.jpg", use_container_width=True)

    with abas[1]:
        st.header("Personagens Importantes")
        
        st.title("Frei Caneca")
        col1, col2 = st.columns([1, 3])
        with col1:
         st.image('https://averdade.org.br/wp-content/uploads/2025/02/P12-_-Frei-Caneca-_-Roberto-Ploeg-1068x1378.jpg', width=150)
        with col2:
         st.subheader('Joaquim da Silva Rabelo')
         st.markdown("""
    **Idade:** 45 anos  
    **Carreira:**  Escritor, clérico católico e político.   
    **Influência:** líder e mártir da Confederação do Equador.      
    **Funções:**  Como jornalista, esteve à frente do Typhis Pernambucano.                 
    """)