import sqlite3
import bcrypt

class Database:
    def __init__(self, db_name="mangaio.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        """Cria tabelas organizadas por área de conhecimento"""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            email TEXT UNIQUE,
            password TEXT,
            role TEXT DEFAULT 'user'
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            area_conhecimento TEXT,
            categoria TEXT,
            pergunta TEXT,
            opcao1 TEXT,
            opcao2 TEXT,
            opcao3 TEXT,
            opcao4 TEXT,
            resposta_correta TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS respostas_usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            quiz_id INTEGER,
            resposta_escolhida TEXT,
            acertou BOOLEAN,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
            FOREIGN KEY (quiz_id) REFERENCES quiz(id)
        )
        """)
        
        self.conn.commit()

    def cadastrar_usuario(self, username, email, password, role="user"):
        """Cadastra um novo usuário com senha criptografada"""
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        try:
            self.cursor.execute("INSERT INTO usuarios (username, email, password) VALUES (?, ?, ?)", 
                                (username, email, hashed_password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def verificar_usuario(self, username, password):
        """Verifica se o usuário existe e se a senha está correta"""
        self.cursor.execute("SELECT password FROM usuarios WHERE username = ?", (username,))
        user = self.cursor.fetchone()
        if user and bcrypt.checkpw(password.encode(), user[0]):
            return True
        return False


    def cadastrar_pergunta(self, area_conhecimento, categoria, pergunta, opcoes, resposta_correta):
        """Admin cadastra novas perguntas no banco de dados"""
        try:
            self.cursor.execute("INSERT INTO quiz (area_conhecimento, categoria, pergunta, opcao1, opcao2, opcao3, opcao4, resposta_correta) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                                (area_conhecimento, categoria, pergunta, *opcoes, resposta_correta))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao cadastrar questão: {e}")
            return False

    def obter_questoes_por_categoria(self, area_conhecimento, categoria):
        """Recupera questões filtradas por área e categoria"""
        self.cursor.execute("SELECT area_conhecimento, categoria, pergunta, opcao1, opcao2, opcao3, opcao4 FROM quiz WHERE area_conhecimento = ? AND categoria = ?", (area_conhecimento, categoria))
        return self.cursor.fetchall()

    def registrar_resposta(self, usuario_id, quiz_id, resposta):
        """Armazena a resposta do usuário e verifica se está correta"""
        self.cursor.execute("SELECT resposta_correta FROM quiz WHERE id = ?", (quiz_id,))
        resposta_correta = self.cursor.fetchone()

        acertou = resposta_correta and resposta == resposta_correta[0]
        
        self.cursor.execute("INSERT INTO respostas_usuario (usuario_id, quiz_id, resposta_escolhida, acertou) VALUES (?, ?, ?, ?)",
                            (usuario_id, quiz_id, resposta, acertou))
        self.conn.commit()