import sqlite3

class ProfessorDao:
    def __init__(self, nome_professor = "professor.db"):
        self.conexao = sqlite3.connect()
        self.cursor = self.conexao.cursor()
    
    def fechar(self):
        self.conexao.close()

class ProfessoresDao(ProfessorDao):

    def criar_tabela(self):
        self.cursor('''
            CREATE TABLE IF NOT EXIST Professores(
                            id INTERGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            disciplica TEXT NOT NULL
                    
            )

    ''')
        
    def inserir_professor(self, nome, disciplina):
        self.cursor.execute('''
            INSERT IN Professores (nome, disciplina) VALUES (?, ?)
                            
    
    ''', (nome, disciplina))
        
    def listar_professores(self):
        self.cursor.execute('SELECT * FROM Professores')
        professores = self.cursor.fetchall()
        print("Lista de Professores")
        for professor in professores:
            print(f"Encontrado: ID = {professor[0]} Nome: {professor[1]} e Disciplina{professor[2]}")

def menu():
    dao=ProfessoresDao
    dao.criar_tabela()

    while True:
        print("Digite 1 para cadastrar professor e disciplina")
        print("Digite 2 para listar professor e disciplina")
        print("Digite 3 para sair")
        opcao = input("Digite uma opção:\n")
        if opcao == "1":
            nome = input("Nome do Professor:\n")
            ministra = input("Disciplina:\n")
            dao.inserir_professor()
            nome2 = input("Nome do próximo Professor")
            ministra2 = input("Nome da próxima disciplina")
            dao.inserir_professor()
        elif opcao == "2":
            dao.listar_professores()
        elif opcao == "3":
            dao.fechar()
            break
        else:
            print("Opção inválida!")
