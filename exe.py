from models.repositorio_cardapio import RepositorioCardapio

rep_cardapio = RepositorioCardapio('db.sqlite')


# Criar
rep_cardapio.criar_cardapio("fastfood", "fastfood", "comida porca") 
rep_cardapio.ler_cardapios()