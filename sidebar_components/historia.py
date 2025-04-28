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

def sidebar_influencias_liberais_republicanas():
    termos = st.tabs(["📖 Introdução", "🕒 Linha do Tempo",
                   "👤 Personagens", "Caça Palavras", "🧠 Quiz"])
    
    with termos[0]:
            st.header("Introdução")
            texto = """A Confederação do Equador foi um movimento separatista influenciado por ideias liberais e republicanas, inspirado pela independência das colônias espanholas e pelos ideais da Revolução Francesa. Defendia a descentralização do poder, o federalismo e a liberdade de imprensa. Os líderes do movimento, como Frei Caneca, Cipriano Barata e Manuel de Carvalho, buscavam romper com o autoritarismo do Império. Esta Confederação surgiu como reação à imposição de Dom Pedro I sobre a Constituição outorgada. Apesar da repressão violenta, o movimento marcou a resistência liberal no Nordeste do Brasil."""
            # Usando HTML para justificar o texto
            html_texto = f"""
            <div style="text-align: justify; font-family: Arial, sans-serif; font-size: 16px;">
                {texto}
            </div>
            """
            # Exibindo o texto justificado no Streamlit
            st.markdown(html_texto, unsafe_allow_html=True)          
            st.video("https://www.youtube.com/watch?v=2vfKe0kBJw4")

    with termos[1]:
            st.header("Linha do Tempo")
            texto = ("""
            - **1789**: Revolução Francesa: difusão dos ideais de liberdade, igualdade e fraternidade.
                          
            - **1817**: Revolução Pernambucana: primeira grande tentativa de independência com ideais republicanos no Brasil.
                          
            - **1821**: Retorno de Dom João VI a Portugal e início do processo de centralização do poder por Dom Pedro I. 

            - **1824 (março)**: Outorga da Constituição de 1824 por Dom Pedro I, centralizadora e imposta sem participação popular.
                        
            - **1824 (julho)**: Eclosão da Confederação do Equador, influenciada pelas ideias liberais e pelo descontentamento com o autoritarismo imperial.
            """)
            html_texto = f"""
            <div style="text-align: justify; font-family: Arial, sans-serif; font-size: 16px;">
                {texto}
            </div>
            """
            st.markdown(html_texto, unsafe_allow_html=True)

    with termos[2]:
            st.header("Personagens Importantes")
            texto = ("""
            - **Frei Caneca (Joaquim do Amor Divino Caneca)** – Religioso, jornalista e intelectual, foi um dos principais ideólogos do movimento. Defensor do republicanismo, federalismo e da liberdade de expressão. Era carismático e articulador político.
                     
            - **Cipriano Barata** – Médico, jornalista e ativista político, conhecido por sua linguagem inflamada e defesa intransigente da liberdade. Atuou em várias revoltas e propagava ideias iluministas e republicanas.
                     
            - **Manuel de Carvalho Paes de Andrade** – Presidente da província de Pernambuco e líder civil da Confederação. Apoiou a causa republicana e foi peça central na proclamação do governo confederado.
                     
            - **Pedro Ivo Veloso da Silveira** – Militar e líder da resistência armada. Comandou as forças confederadas no interior, sendo símbolo da luta até os últimos momentos do movimento.
            """)

            html_texto = f"""
            <div style="text-align: justify; font-family: Arial, sans-serif; font-size: 16px;">
                {texto}
            </div>
            """
            st.markdown(html_texto, unsafe_allow_html=True)

    with termos[3]:

        st.header("Caça-palavras")
        st.write("🎮 Aqui é onde o jogo vai!")
        html_code = """
        <style>
        table {
            border-collapse: collapse;
            margin-bottom: 10px;
            background-color: white;
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
        const words = ["MOVIMENTO", "LIBERAIS", "SEPARATISTA", "AUTORITARISMO", "DESCENTRALIZADO", "REVOLUÇÃO", "REPRESSÃO", "NORDESTE", "VIOLÊNCIA", "COLÔNIAS", "OUTORGADA", "IMPOSIÇÃO", "CONSTITUIÇÃO"];
        let foundWords = [];
        let selectedCells = [];

        const grid = [
            ["M", "T", "R", "E", "A", "M", "L", "I", "E", "A", "M", "L", "I"],
            ["O", "U", "T", "O", "R", "G", "D", "A", "R", "E", "A", "M", "A"],
            ["V", "A", "R", "E", "P", "R", "E", "S", "S", "Ã", "O", "A", "I"],
            ["I", "M", "C", "O", "S", "I", "Ç", "Ã", "O", "E", "U", "N", "C"],
            ["M", "U", "C", "O", "L", "Ô", "N", "I", "A", "S", "I", "E", "N"],
            ["E", "T", "R", "R", "E", "A", "M", "L", "I", "A", "M", "L", "Ê"],
            ["N", "Y", "T", "N", "O", "R", "D", "E", "S", "T", "E", "A", "L"],
            ["T", "A", "V", "E", "S", "C", "I", "P", "R", "I", "A", "N", "O"],
            ["O", "S", "E", "P", "A", "R", "A", "T", "I", "S", "T", "A", "I"],
            ["L", "I", "B", "E", "R", "A", "I", "S", "K", "D", "Q", "P", "V"],
            ["O", "M", "S", "I", "R", "A", "T", "I", "R", "O", "T", "U", "A"]
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