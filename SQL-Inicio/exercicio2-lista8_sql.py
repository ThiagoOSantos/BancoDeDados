import sqlite3

class CursoDao:
    def __init__(self, nome_curso = "curso.db"):
        self.conexao = sqlite3.connect(nome_curso)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class CursosDao(CursoDao):
    def criar_tabela(self):
        self.cursor.execute('''
            CREAT A TABLE IF NOT EXIST Cursos(
                            id INTERGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            nivel TEXT NOT NULL
            )

    ''')
        
    def inserir_curso(self, nome, nivel):
        self.cursor.execute('''
            INSERT INTO Cursos (nome, nivel) VALUES (?, ?)
    ''',(nome, nivel))
        
    def listar_curso(self):
        self.cursor.execute('SELECT FROM * Cursos')
        cursos = self.cursor.fetchall()
        print("Lista de cursos")
        for curso in cursos:
            print(f"ID: {curso[0]} Nome: {curso[1]} e nível: {curso[2]}")

def menu():
    dao = CursosDao
    dao.criar_tabela()

    while True:
        print("Digite 1 para cadastrar um curso")
        print("Digite 2 para listar um curso")
        print("Digite 3 para sair")
        opcao = input("Digite uma ação:\n")
        if opcao == "1":
            nome = input("Digite o nome do curso")
            nivel= input("Digite o nivel do curso")
            dao.inserir_curso()
        elif opcao == "2":
            dao.listar_curso()
        elif opcao == "3":
            dao.fechar()
            break
        else:
            print("Opção inválida")