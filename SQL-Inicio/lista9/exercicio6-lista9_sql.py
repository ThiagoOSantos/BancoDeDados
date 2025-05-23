import sqlite3

class ConexaoBanco:
    def __init__(self, nome_banco="Xadres.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class Ranking(ConexaoBanco):

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ranking(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            pontuacao INTEGER NOT NULL
                )
    ''')
    
    def inserir_aluno(self, nome, pontuacao):
        self.cursor.execute('''
            INSERT INTO ranking (nome, pontuacao) VALUES (?, ?)
        ''', (nome, pontuacao))
        self.conexao.commit()
        print(f'Aluno "{nome}" com pontuação {pontuacao} foi cadastrado!')

    def buscar_por_pontuacao(self, min_pontuacao):
        self.cursor.execute('SELECT * FROM ranking WHERE pontuacao >= ?', (min_pontuacao,))
        alunos = self.cursor.fetchall()

        if alunos:
            print("\nAlunos com pontuação mínima de", min_pontuacao, ":")
            for aluno in alunos:
                print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Pontuação: {aluno[2]}")
        else:
            print(f"Nenhum aluno encontrado com pontuação maior ou igual a {min_pontuacao}.")

    def fechar(self):
        self.conexao.close()

# Exemplo de uso
dao = Ranking()
dao.criar_tabela()

# Inserindo alunos
dao.inserir_aluno("Carlos", 85)
dao.inserir_aluno("Ana", 90)
dao.inserir_aluno("Marcos", 75)

# Buscando alunos com pontuação mínima
pontuacao_min= int(input("Digite a pontuação mínima para buscar:\n"))
dao.buscar_por_pontuacao(pontuacao_min)

dao.fechar()

