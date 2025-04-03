import logging
import pandas as pd
from glob import glob
from db import get_connection
from pathlib import Path

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s - %(message)s')


def testa_mysql():
    logging.info("Testando conexão com MySQL...")
    try:
        with get_connection() as conn:
            logging.info("Conexão com MySQL estabelecida.")
    except Exception as e:
        logging.error(f"Erro na conexão com MySQL: {e}")


def verifica_csvs(caminho_csvs):
    arquivos = glob(str(Path(caminho_csvs)))
    for arq in arquivos:
        logging.info(f"Verificando arquivo: {arq}")
        try:
            df = pd.read_csv(arq, encoding="latin1", sep=';', nrows=5)
            logging.info(f"Colunas encontradas: {df.columns.tolist()}")
        except Exception as e:
            logging.error(f"Erro ao abrir {arq}: {e}")


if __name__ == "__main__":
    testa_mysql()
    verifica_csvs("dados/csvs/*.csv")
    verifica_csvs("dados/cadop/*.csv")
