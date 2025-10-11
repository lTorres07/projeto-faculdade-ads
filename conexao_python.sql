CREATE DATABASE IF NOT EXISTS cinema;
USE cinema;

CREATE TABLE IF NOT EXISTS ingressos (
    id INT NOT NULL AUTO_INCREMENT,
    filme VARCHAR(100) NOT NULL,
    quantidade INT NOT NULL,
    PRIMARY KEY (id)
) DEFAULT CHARSET = utf8;

CREATE TABLE IF NOT EXISTS clientes (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14),
    telefone VARCHAR(20),
    cidade VARCHAR(50),
    PRIMARY KEY (id)
) DEFAULT CHARSET = utf8;

-- Para testar:
SELECT * FROM ingressos;
SELECT * FROM clientes;
