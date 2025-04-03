-- Criação do banco, se ainda não existir
CREATE DATABASE IF NOT EXISTS ans_dados DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE ans_dados;

-- Criação da tabela de operadoras ativas
DROP TABLE IF EXISTS operadoras_ativas;

CREATE TABLE operadoras_ativas (
    registro_ans INT PRIMARY KEY,
    cnpj VARCHAR(20),
    razao_social TEXT,
    nome_fantasia TEXT,
    modalidade VARCHAR(100),
    uf VARCHAR(5),
    municipio VARCHAR(100),
    data_registro DATE
);
