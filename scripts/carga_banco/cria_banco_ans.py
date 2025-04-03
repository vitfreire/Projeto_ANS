import logging
import os
from api.db import get_connection
import sys
from pathlib import Path

# Adiciona o diretório raiz do projeto ao sys.path
project_root = str(Path(__file__).resolve().parent.parent.parent.resolve())
sys.path.insert(0, project_root)

# Para depuração: imprima sys.path e confirme
# print("sys.path:", sys.path)


logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s - %(message)s')


def criar_banco_e_tabelas():
    with get_connection() as conn:
        cursor = conn.cursor()
        # Exemplo de criação de tabela
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS operadoras_ativas (
                registro_ans INT PRIMARY KEY,
                cnpj VARCHAR(20),
                razao_social VARCHAR(255),
                nome_fantasia VARCHAR(255),
                modalidade VARCHAR(50),
                uf VARCHAR(2),
                municipio VARCHAR(255),
                data_registro DATE
            );
        """)
        conn.commit()
        logging.info("Banco e tabelas criados com sucesso.")


if __name__ == "__main__":
    try:
        criar_banco_e_tabelas()
    except Exception as e:
        logging.error(f"Erro ao criar banco/tabelas: {e}")
        sys.exit(1)
