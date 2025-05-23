import sqlite3

class LivroDao:
    def __init__(self,nome_livros = "livros.db"):
        self.conexao = sqlite3.connect(nome_livros) #Sempre que for começar a função construtora da classe, utilizar a conexao = sqlite3.connect('nome do banco' = 'banco.db')
        self.cursor = self.conexao.cursor() #seguido de self.cursor = self.conexao.cursor() esses sempre serão os comandos padrões da classe primaria
    
    def fechar(self):
        self.conexao.close()

class LivrosDao(LivroDao):
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros(
                            id INTEGER PRIMARY KEY,
                            titulo TEXT NOT NULL,
                            autor TEXT NOT NULL
                            
            )

    ''')
    def inserir_livro(self, titulo, autor):
        self.cursor.execute('''
            INSERT INTO livros (titulo, autor) VALUES (?,?)
    ''',(titulo, autor))
            
    def listar_livros(self):
        self.cursor.execute('SELECT * FROM livros')
        livros = self.cursor.fetchall()
        print("Lista de Livros")
        for livro in livros:
            print(f"ID: {livro[0]} do Livro: {livro[1]} do Autor: {livro[2]}")

def menu():
    dao = LivrosDao()
    dao.criar_tabela()

    while True:
        print("Digite 1 para cadastrar livro \n")
        print("Digite 2 para ver livro \n")
        print("Digite 3 para sair \n")
        opcao = input("Digite a opcao escolhida \n")
        if opcao == "1":
            titulo = input("Digite o nome do titulo \n")
            autor = input("Digite o nome do autor \n")
            dao.inserir_livro(titulo,autor)
        elif opcao =="2":
            dao.listar_livros()
        elif opcao =="3":
            dao.fechar()
            print("Encerrando o sitema \n")
            break
        else:
            print("Opção inválida")

menu()