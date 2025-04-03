import pandas as pd
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s - %(message)s')


def test_operadoras_csv():
    csv_file = Path("dados") / "cadop" / "cadop_tratado.csv"
    df = pd.read_csv(csv_file)
    assert not df.empty, "CSV de operadoras está vazio."
    for coluna in ['registro_ans', 'cnpj', 'nome_fantasia']:
        assert coluna in df.columns, f"Coluna {coluna} não encontrada."


def test_dados_contabeis_csv():
    csv_file = Path("dados") / "dados_contabeis.csv"
    df = pd.read_csv(csv_file)
    assert not df.empty, "CSV de dados contábeis está vazio."
    for coluna in ['registro_ans', 'valor', 'competencia']:
        assert coluna in df.columns, f"Coluna {coluna} não encontrada."


if __name__ == "__main__":
    try:
        test_operadoras_csv()
        logging.info("Teste de operadoras CSV passou.")
        test_dados_contabeis_csv()
        logging.info("Teste de dados contábeis CSV passou.")
    except AssertionError as e:
        logging.error(f"Teste falhou: {e}")
        exit(1)
