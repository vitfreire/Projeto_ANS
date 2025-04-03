from api.db import get_connection
import os
import sys
import logging
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s - %(message)s')

TABELAS = [
    "demonstracoes_contabeis",
    "operadoras_ativas"
]


def limpar_tabelas():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            for tabela in TABELAS:
                logging.info(f"Limpando tabela: {tabela}")
                cursor.execute(f"DELETE FROM {tabela}")
            conn.commit()
    logging.info("Todas as tabelas foram limpas.")


if __name__ == "__main__":
    limpar_tabelas()
