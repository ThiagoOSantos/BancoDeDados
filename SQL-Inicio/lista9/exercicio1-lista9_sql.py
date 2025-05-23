import sqlite3

class Cantina:
    def __init__(self, nome_banco= "Cantina.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

class LancheDao(Cantina):
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Lanches(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            preco INTEGER NOT NULL
            )

    ''')
        
    def criar_lanche(self, nome, preco):
        self.cursor.execute('''
            INSERT INTO Lanches (nome, preco) VALUES (?,?)
    ''', (nome, preco))
        self.conexao.commit()
        print(f"Lanche: {nome} de preço R${preco} Cadastrado")
    
    
    
    def listar_lanche(self):
        self.cursor.execute('SELECT * FROM Lanches')
        Lanches = self.cursor.fetchall()
        print("Lista de Lanches")
        for lanche in Lanches:
            print(f"ID do lanche: {lanche[0]}, Nome: {lanche[1]} e preco: R${lanche[2]}")



def menuCantina():
    dao = LancheDao()
    dao.criar_tabela()

    while True:
        print("Olá, bem vindo a cafeteria do Senac! Digite 1 para adicionar um lanche")
        print("Digite 2 para listar os lanches")
        print("Digite 3 para sair")
        opcao = input("Digite a ação desejada:\n")
        if opcao == "1":
            nome = input("Digite o nome do lanche:\n")
            preco = float(input("Digite o valor do lanche:\n"))
            dao.criar_lanche(nome,preco)
        elif opcao == "2":
            dao.listar_lanche()
        elif opcao == "3":
            dao.fechar()
            print("Cadastros encerrados, fim do programa")
            break
        else:
            print("Opcão inválida")

menuCantina()
