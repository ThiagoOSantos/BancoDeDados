import sqlite3

class Clientes:
    def __init__(self, nome_cliente="Clientes.db"):
        self.conexao = sqlite3.connect(nome_cliente)#Sempre que for começar a função construtora da classe, utilizar a conexao = sqlite3.connect('nome do banco' = 'banco.db')
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class ClienteDao(Clientes):

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXIST Clientes(
                            id INTERGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL
            )
    ''')

    def inserir_cliente(self, nome, email):
        self.cursor.execute('''
            INSERT INTO Clientes (nome, email) VALUES (?,?)
                               
    ''', (nome, email))
    
    def listar_clientes(self):
        self.cursor.execute('SELECT * FROM Clientes')
        clientesdao = self.cursor.fetchall()
        print("lista de clientes")
        for cliente in clientesdao:
            print(f"ID - {cliente[0]}, Nome {cliente[1]} e email: {cliente[2]}")

def menu():
    dao = ClienteDao
    dao.criar_tabela

    while True:
        print("Digite 1 para cadastrar cliente")
        print("Digite 2 para listar clientes")
        print("Digite 3 para listar sair")
        opcao = input("O que deseja fazer? \n")
        if opcao == "1":
            nome = input("Digite o nome do cliente:\n")
            email = input("Digite o email do cliente:\n")
            dao.inserir_cliente
        elif opcao == "2":
            dao.listar_clientes
        elif opcao == "3":
            dao.fechar
            print("Encerrando")
            break
        else:
            print("Opção inválida")

menu()