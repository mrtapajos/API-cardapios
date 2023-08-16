import sqlite3

class RepositorioCardapio(object):
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
    def criar_cardapio(self, codigo: str, nome: str, descricao: str) -> None:
        self.abrir_conexao()

        code = "INSERT OR IGNORE INTO cardapio (codigo, nome, descricao) VALUES (?, ?, ?)"
        self.cursor.execute(code, (codigo, nome, descricao))

        self.connection.commit()
        self.fechar_conexao()

    # READ
    def ler_cardapios(self) -> list:
        self.abrir_conexao()

        self.cursor.execute("SELECT * FROM cardapio")
        leitura = self.cursor.fetchall()

        self.fechar_conexao()
        return leitura
    
    def ler_entidade(self, codigo: str):
        self.abrir_conexao()
        self.cursor.execute("SELECT * FROM cardapio WHERE codigo = ?", (codigo,))
        leitura = self.cursor.fetchone()

        self.fechar_conexao()
        return leitura
        

    # UPDATE
    def alterar_cardapio(self, codigo, nome, descricao) -> None:
        self.abrir_conexao()

        code = "UPDATE cardapio SET nome = ?, descricao = ? WHERE codigo = ?"
        self.cursor.execute(code, (nome, descricao, codigo))
        
        self.fechar_conexao()

    # DELETE
    def deletar_cardapio(self, codigo: str) -> None:
        self.abrir_conexao()

        code = "DELETE FROM cardapio WHERE codigo = ?"
        self.cursor.execute(code, (codigo,))

        self.connection.commit()
        self.fechar_conexao()

    