# from dotenv import dotenv_values
from models.repositorio_cardapio import RepositorioCardapio
from models.repositorio_produto import RepositorioProduto

# ENV = dotenv_values()
NOME_DB = "db.sqlite"

def obter_rep_cardapio():
    return RepositorioCardapio(NOME_DB)

def obter_rep_produtos():
    return RepositorioProduto(NOME_DB)