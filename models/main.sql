PRAGMA foreign_keys=ON;

BEGIN TRANSACTION;

CREATE TABLE cardapio (
    codigo TEXT PRIMARY KEY,
    nome TEXT UNIQUE NOT NULL,
    descricao TEXT NOT NULL
);

CREATE TABLE produto (
    codigo TEXT PRIMARY KEY,
    nome TEXT UNIQUE NOT NULL,
    descricao TEXT NOT NULL,
    preco INTEGER NOT NULL,
    restricao TEXT NOT NULL,
    codigo_cardapio TEXT NOT NULL,

    FOREIGN KEY (codigo_cardapio) REFERENCES cardapio(codigo)
    ON UPDATE RESTRICT ON DELETE RESTRICT

);

INSERT OR IGNORE INTO cardapio (codigo, nome, descricao) VALUES ('vegano', 'vegano', 'comidas veganas');
        
INSERT OR IGNORE INTO produto (codigo, nome, descricao, preco, restricao, codigo_cardapio) VALUES ('pizza vegana', 'pizza vegana', 'pizza feita para pessoas vegana (sem derivados de animais)', 35, 'vegano', 'vegano');

COMMIT;