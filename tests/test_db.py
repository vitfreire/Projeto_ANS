from api.db import get_connection
import sys
import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s - %(message)s')

# Adiciona a pasta api/ ao sys.path
api_path = Path(__file__).resolve().parent.parent / "api"
sys.path.insert(0, str(api_path))
logging.info(f"Pasta API adicionada ao sys.path: {api_path}")


def test_mysql_connection():
    try:
        with get_connection() as conn:
            assert conn.open, "Conexão não está aberta."
            logging.info("Conexão com MySQL estabelecida com sucesso.")
    except Exception as e:
        assert False, f"Erro de conexão com banco: {e}"


if __name__ == "__main__":
    test_mysql_connection()
