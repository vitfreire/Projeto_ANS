from scripts.utilitarios.download_utils import baixar_arquivo
import os
import sys
import logging
import pandas as pd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s - %(message)s')

csv_bruto = Path("dados") / "cadop" / "Relatorio_cadop.csv"
csv_tratado = Path("dados") / "cadop" / "cadop_tratado.csv"
csv_bruto.parent.mkdir(parents=True, exist_ok=True)

URL = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv"


def tratar_csv():
    logging.info("Processando e estruturando dados...")
    try:
        df = pd.read_csv(csv_bruto, sep=';', encoding='utf-8')
    except Exception as e:
        logging.error(f"Erro ao ler {csv_bruto}: {e}")
        raise

    df.rename(columns={
        'Registro_ANS': 'registro_ans',
        'CNPJ': 'cnpj',
        'Razao_Social': 'razao_social',
        'Nome_Fantasia': 'nome_fantasia',
        'Modalidade': 'modalidade',
        'UF': 'uf',
        'Cidade': 'municipio',
        'Data_Registro_ANS': 'data_registro'
    }, inplace=True)
    df = df[['registro_ans', 'cnpj', 'razao_social', 'nome_fantasia',
             'modalidade', 'uf', 'municipio', 'data_registro']]
    df.to_csv(csv_tratado, index=False, encoding="utf-8")
    logging.info(f"Dados tratados salvos em: {csv_tratado}")


if __name__ == "__main__":
    try:
        baixar_arquivo(URL, csv_bruto)
        tratar_csv()
        logging.info(f"Arquivo baixado em: {csv_bruto}")
    except Exception as e:
        logging.error(f"Erro no processamento: {e}")
        sys.exit(1)
