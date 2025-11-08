-- Criar banco de dados
CREATE DATABASE IF NOT EXISTS cinema;
USE cinema;

-- Tabela de ingressos
CREATE TABLE IF NOT EXISTS ingressos (
    id INT NOT NULL AUTO_INCREMENT,
    filme VARCHAR(100) NOT NULL,
    quantidade INT NOT NULL,
    PRIMARY KEY (id)
) DEFAULT CHARSET = utf8;

-- Tabela de clientes
CREATE TABLE IF NOT EXISTS clientes (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14),
    telefone VARCHAR(20),
    cidade VARCHAR(50),
    PRIMARY KEY (id)
) DEFAULT CHARSET = utf8;

-- Tabela de sessões
CREATE TABLE IF NOT EXISTS sessoes (
    id INT NOT NULL AUTO_INCREMENT,
    horario VARCHAR(10) NOT NULL,
    sala VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
) DEFAULT CHARSET = utf8;

-- Testar
SELECT * FROM ingressos;
SELECT * FROM clientes;
SELECT * FROM sessoes;
