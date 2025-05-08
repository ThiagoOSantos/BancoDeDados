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
            INSER IN Professores (nome, disciplina) VALUES (?, ?)
                            
    
    ''', (nome, disciplina))
        
    def listar_professores(self):
        self.cursor.execute('SELECT FROM * Professores')
        professores = self.cursor.fetchall()
        print("Lista de Professores")
        for professor in professores:
            print(f"ID: {professor[0]} Nome: {professor[1]} e Disciplina{professor[2]}")
        