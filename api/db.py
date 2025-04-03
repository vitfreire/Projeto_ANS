import os
import pymysql
import logging
from dotenv import load_dotenv
from pathlib import Path

# Carrega as variáveis de ambiente a partir do arquivo .env na raiz do projeto
dotenv_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=dotenv_path)


logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s - %(message)s')


def get_connection():
    host = os.getenv("MYSQL_HOST")
    user = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    database = os.getenv("MYSQL_DATABASE")

    # Validação: permite senha vazia, mas não permite que as variáveis estejam ausentes (None)
    if host is None or user is None or database is None:
        logging.error(
            "As variáveis de ambiente para conexão com MySQL não estão definidas corretamente.")
        raise ValueError(
            "Variáveis de ambiente de conexão com MySQL não definidas.")

    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password if password is not None else "",
            database=database,
            charset="utf8mb4"
        )
        logging.info("Conexão com MySQL estabelecida com sucesso.")
        return connection
    except pymysql.MySQLError as e:
        logging.error(f"Erro ao conectar com MySQL: {e}")
        raise
