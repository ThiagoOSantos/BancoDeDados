import sqlite3

class VisitantesDao:
    def __init__(self, nome_banco = "Visitantes.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class Visitantes(VisitantesDao):
    
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS visitantes(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            motivo TEXT NOT NULL
            )
    ''')
    def inserir_visitante(self, nome, motivo):
        self.cursor.execute('''
            INSERT INTO visitantes (nome, motivo) VALUES (?,?)

    ''', (nome, motivo))
        self.conexao.commit()
        print(f"O visitante {nome} que veio pelo {motivo} foi cadastrado!")

    def listar_visitante(self):
        self.cursor.execute('SELECT * FROM visitantes')
        visitantes = self.cursor.fetchall()
        print("Lista de visitantes \n")
        for visitante in visitantes:
            print(f"Visitante de nome {visitante[1]} e motivo {visitante[2]} passou por aqui")

    def excluir_visitante(self, nome):
        self.cursor.execute('DELETE FROM visitantes WHERE nome =?', (nome,))
        self.conexao.commit()
        print(f"Visitante de nome {nome} excluído")

def menu():
    dao = Visitantes()
    dao.criar_tabela()
    
    while True:
        print("1-inserir visitante")
        print("2-listar visitante")
        print("3- apagar visitante")
        print("4 - sair")
        opcao = input("escolha uma opção:\n")
        if opcao == "1":
            nome = input("Digite o nome do visitante:\n")
            motivo = input("Digite o motivo:\n")
            dao.inserir_visitante(nome, motivo)
        elif opcao == "2":
            dao.listar_visitante()
        elif opcao == "3":
            nome = input("quem deseja excluir?")
            dao.excluir_visitante(nome)
        elif opcao == "4":
            dao.fechar()
            print("Encerrando o sistema")
            break
        else:
            print("Opção inválida")

menu()