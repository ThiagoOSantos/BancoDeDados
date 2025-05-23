import sqlite3

class BancoDB():
    def __init__(self, nome_banco="Loja.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class CodeWear(BancoDB):

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Camisetas(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            cor TEXT NOT NULL,
                            quantidade INTEGER                            
                )
    ''')
    def adicionar_camisa(self, nome, cor, quantidade):
        self.cursor.execute('''
            INSERT INTO Camisetas (nome, cor, quantidade) VALUES (?,?,?)                           
    ''', (nome, cor, quantidade))
        self.conexao.commit()
        print(f"modelo de nome {nome}, cor {cor}, e quantidade {quantidade} inseridos com sucesso")
        
    def atualizar_quantidade(self, nome, nova_quantidade):
        self.cursor.execute('UPDATE Camisetas SET quantidade =? WHERE nome =?', (nome, nova_quantidade))
        self.conexao.commit()
        print(f"Produto {nome} com nova {nova_quantidade} atualizado")

    def listar_camisas(self):
        self.conexao.execute('SELECT * FROM Camisetas')
        camisas = self.cursor.fetchall()
        print("Lista de camisas")
        for camisa in camisas:
            print(f"ID - {camisa[0]}, nome: {camisa[1]} tem {camisa[2]} unidades")

def menu():
    dao = CodeWear()
    dao.criar_tabela()

    while True:
        print("1-inserir produto")
        print("2-listar produto")
        print("3- atualizar quantidade")
        print("4 - deletar produto")
        opcao = input("escolha uma opção:\n")
        if opcao == "1":
            nome = input("Digite o nome do produto: \n")
            cor = input("Digite a cor do produto: \n")
            quantidade = int(input("Digite a quantidade do produto: \n"))
            dao.adicionar_camisa(nome,cor, quantidade)
        elif opcao == "2":
            dao.listar_camisas()
        elif opcao == "3":
            nome = input("qual produto pra alterar mesmo? \n")
            quantidade = int(input("qual a nova quantidade? \n"))
            dao.atualizar_quantidade(nome, quantidade)
        elif opcao == "4":
            dao.fechar()
            print("Encerrando o sistema")
            break
        else:
            print("Opção inválida")

menu()