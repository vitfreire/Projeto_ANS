-- Cria o banco de dados com charset adequado
CREATE DATABASE IF NOT EXISTS ans_dados DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE ans_dados;

-- Tabela: operadoras_ativas
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

-- Tabela: demonstracoes_contabeis
DROP TABLE IF EXISTS demonstracoes_contabeis;

CREATE TABLE demonstracoes_contabeis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    registro_ans INT,
    competencia DATE,
    codigo_contabil VARCHAR(20),
    conta_contabil TEXT,
    valor DECIMAL(20,2),
    origem_arquivo VARCHAR(100)
);
