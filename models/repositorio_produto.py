import sqlite3

class RepositorioProduto(object):
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco
        self.connection = None
        self.cursor = None

    def abrir_conexao(self) -> None:
        self.connection = sqlite3.connect(self.nome_banco)
        self.cursor = self.connection.cursor()

    def fechar_conexao(self) -> None:
        self.cursor.close()
        self.connection.close()
        
        self.connection = None
        self.cursor = None

    # ------------ CRUD ------------

    # CREATE 
    def criar_produto(self, codigo: str, nome: str, descricao: str, preco: float, restricao: str, codigo_cardapio: str) -> None:
        self.abrir_conexao()

        code = "INSERT OR IGNORE INTO produto (codigo, nome, descricao, preco, restricao, codigo_cardapio) VALUES (?, ?, ?, ?, ?, ?)"

        self.cursor.execute(code, (codigo, nome, descricao, preco, restricao, codigo_cardapio))
        self.connection.commit()

        self.fechar_conexao()
    
    # READ
    def listar_produtos(self) -> list:
        self.abrir_conexao()

        self.cursor.execute("SELECT * FROM produto")
        leitura = self.cursor.fetchall()
        
        self.fechar_conexao()
        return leitura
    
    def ler_entidade(self, codigo):
        self.abrir_conexao()

        self.cursor.execute("SELECT * FROM produto WHERE codigo = ?", (codigo,))
        leitura = self.cursor.fetchone()
        
        self.fechar_conexao()
        return leitura
    
    # UPDATE
    def alterar_produto(self, nome: str, descricao: str, preco: float, restricao: str, codigo_cardapio: str, codigo: str) -> None:
        self.abrir_conexao()
        code = "UPDATE produto SET nome = ?, descricao = ?, preco = ?, restricao = ?, codigo_cardapio = ? WHERE codigo = ?"

        self.cursor.execute(code, (nome, descricao, preco, restricao, codigo_cardapio, codigo))
        self.connection.commit()

        self.fechar_conexao()
        
    # DELETE
    def deletar_produto(self, codigo: str) -> None:
        self.abrir_conexao()

        code = "DELETE FROM produto WHERE codigo = ?"
        self.cursor.execute(code, (codigo,))

        self.connection.commit()
        self.fechar_conexao()