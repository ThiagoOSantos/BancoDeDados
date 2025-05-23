import sqlite3

class ConexaoBanco:
    def __init__(self, nome_banco = "Loja-gamer.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class LojaDAO(ConexaoBanco): #DAO = Data Access Objet
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Gamers(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            preco INTERGER NOT NULL
            )                
    ''')
        
    def inserir_produto(self, nome, preco):
        self.cursor.execute('''
            INSERT INTO Gamers (nome,preco) VALUES (?, ?)
    ''', (nome,preco))
        self.conexao.commit()
        print(f"Produto {nome} de preco {preco} inserido com sucesso")

    def listar_produtos(self):
        self.cursor.execute('SELECT * FROM Gamers')
        produtos = self.cursor.fetchall()
        print("Lista de Produtos: \n")
        for produto in produtos:
            print(f"ID: {produto[0]} - Nome: {produto[1]} - Idade: {produto[2]}")


    def buscar_por_nome(self,nome): #criação de uma função que fará a busca de item específico dentro do banco de dados
        self.cursor.execute('SELECT * FROM Gamers WHERE nome = ?', (nome))# sempre utilizar a função cursor para iniciar funções no banco de dadnos,  # (formatação do select exige o * após 'SELECT')
        resultado = self.cursor.fetchall()
        if resultado:
            for produto in resultado:
                print(f"Encontrado: ID {produto[0]}, Nome {produto[1]}, preço {produto[2]}")
        else:
            print("Produto não encontrado")

    def atualizar_preco(self, nome, novo_preco):
        self.cursor.execute('UPDATE Gamers SET preco =? WHERE nome =?',(nome, novo_preco))
        self.conexao.commit()
        print(f"Produto de {nome} foi atualizado para {novo_preco}")                                                                                

    def deletar_produto(self, nome):
        self.cursor.execute('DELETE FROM Gamers WHERE nome =?', (nome))
        self.conexao.commit()
        print(f"Produto {nome} foi removido com sucesso.")

def menu():
    dao = LojaDAO()
    dao.criar_tabela()

    while True:
        print("1-inserir produto")
        print("2-listar produto")
        print("3- atualizar preço")
        print("4 - deletar produto")
        opcao = input("escolha uma opção:\n")
        if opcao == "1":
            nome = input("Digite o nome do produto:\n")
            preco = int(input("Digite o valor do produto:\n"))
            dao.inserir_produto(nome,preco)
        elif opcao == "2":
            dao.listar_produtos()
        elif opcao == "3":
            nome = input("qual produto pra alterar mesmo?\n")
            preco = int(input("qual o novo preço?\n"))
            dao.atualizar_preco()
        elif opcao == "4":
            nome = input("Qual o produto pra apagar?")
            dao.deletar_produto(nome)
        elif opcao == "5":
            dao.fechar()
            print("Encerrando o sistema")
            break
        else:
            print("Opção inválida")

menu()