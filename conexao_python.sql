-- Banco de Dados: Cinema
DROP DATABASE IF EXISTS cinema;
CREATE DATABASE cinema;
USE cinema;


-- Tabela: ingressos
CREATE TABLE IF NOT EXISTS ingressos (
    id INT NOT NULL AUTO_INCREMENT,
    filme VARCHAR(100) NOT NULL,
    quantidade INT NOT NULL,
    PRIMARY KEY (id)
) DEFAULT CHARSET = utf8;


-- Tabela: clientes
CREATE TABLE IF NOT EXISTS clientes (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14),
    telefone VARCHAR(20),
    cidade VARCHAR(50),
    ingresso_id INT,  -- FK para ingressos
    PRIMARY KEY (id),
    FOREIGN KEY (ingresso_id) REFERENCES ingressos(id) ON DELETE SET NULL
) DEFAULT CHARSET = utf8;


-- Tabela: sessoes
CREATE TABLE IF NOT EXISTS sessoes (
    id INT NOT NULL AUTO_INCREMENT,
    horario VARCHAR(10) NOT NULL,
    sala VARCHAR(50) NOT NULL,
    ingresso_id INT,  -- FK para ingressos
    PRIMARY KEY (id),
    FOREIGN KEY (ingresso_id) REFERENCES ingressos(id) ON DELETE SET NULL
) DEFAULT CHARSET = utf8;


-- Tabela: pagamento
CREATE TABLE IF NOT EXISTS pagamento (
    id INT NOT NULL AUTO_INCREMENT,
    ingresso_id INT NOT NULL,  -- FK para ingressos
    tipo VARCHAR(20) NOT NULL, -- meia ou inteira
    valor_total DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (ingresso_id) REFERENCES ingressos(id) ON DELETE CASCADE
) DEFAULT CHARSET = utf8;

-- Testes
SELECT * FROM ingressos;
SELECT * FROM clientes;
SELECT * FROM sessoes;
SELECT * FROM pagamento;