import sqlite3

if __name__ == "__main__":
    with open('main.sql', 'r') as file:
        sql_code = file.read()

    # ABRINDO CONEXÃO E CURSOR
    connection = sqlite3.connect('db.sqlite')
    cursor = connection.cursor()

    cursor.executescript(sql_code) # STRING SENDO USADA

#     cursor.executescript(
#         '''INSERT OR IGNORE INTO cardapio (codigo, nome, descricao) VALUES ('vegano', 'vegano', 'comidas veganas');
        
#         INSERT OR IGNORE INTO produto (codigo, nome, descricao, preco, restricao, codigo_cardapio) VALUES ('pizza vegana', 'pizza vegana', 'pizza feita para pessoas vegana (sem derivados de animais)', 35, 'vegano', 'vegano');'''
# )
    connection.commit()

    # FECHAR 
    cursor.close()
    connection.close()