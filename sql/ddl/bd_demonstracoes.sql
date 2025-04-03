USE ans_dados;

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
