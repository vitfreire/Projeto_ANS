from scripts.utilitarios.download_utils import baixar_arquivo
import os
import sys
import logging
import zipfile
import pandas as pd
import requests
from glob import glob
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s - %(message)s')

URL_BASE = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis"
ANOS = ["2023", "2024"]

zips_dir = Path("dados") / "zips"
csvs_dir = Path("dados") / "csvs"
zips_dir.mkdir(parents=True, exist_ok=True)
csvs_dir.mkdir(parents=True, exist_ok=True)


def baixar_arquivos():
    for ano in ANOS:
        for trimestre in range(1, 5):
            nome_arquivo = f"{trimestre}T{ano}.zip"
            url = f"{URL_BASE}/{ano}/{nome_arquivo}"
            destino = zips_dir / nome_arquivo
            if not destino.exists():
                logging.info(
                    f"Iniciando download de {nome_arquivo} ({ano})...")
                try:
                    baixar_arquivo(url, destino)
                except Exception as e:
                    logging.error(f"Erro ao baixar {nome_arquivo}: {e}")
            else:
                logging.info(f"Arquivo {nome_arquivo} já existe.")


def extrair_arquivos():
    for zip_path in glob(str(zips_dir / "*.zip")):
        try:
            with zipfile.ZipFile(zip_path, 'r') as zf:
                logging.info(f"Extraindo {zip_path}...")
                zf.extractall(str(csvs_dir))
        except Exception as e:
            logging.error(f"Erro ao extrair {zip_path}: {e}")


def unir_csvs():
    arquivos = glob(str(csvs_dir / "*.csv"))
    dfs = []

    for arq in arquivos:
        try:
            df = pd.read_csv(arq, encoding="utf-8", sep=';', dtype=str)
            df["origem_arquivo"] = Path(arq).name
            dfs.append(df)
        except Exception as e:
            logging.error(f"Erro ao ler {arq}: {e}")

    if not dfs:
        logging.warning("Nenhum CSV válido encontrado.")
        return

    df_final = pd.concat(dfs, ignore_index=True)
    df_final.rename(columns={
        'DATA': 'competencia',
        'REG_ANS': 'registro_ans',
        'CD_CONTA_CONTABIL': 'codigo_contabil',
        'DESCRICAO': 'conta_contabil',
        'VL_SALDO_FINAL': 'valor'
    }, inplace=True)
    df_final = df_final[['registro_ans', 'competencia',
                         'codigo_contabil', 'conta_contabil', 'valor', 'origem_arquivo']]
    df_final.dropna(subset=["valor"], inplace=True)

    try:
        df_final["valor"] = df_final["valor"].str.replace(
            ".", "", regex=False).str.replace(",", ".", regex=False).astype(float)
        df_final["competencia"] = pd.to_datetime(
            df_final["competencia"], errors="coerce", format="%Y-%m-%d")
    except Exception as e:
        logging.error(f"Erro na conversão dos dados: {e}")
        raise

    destino_csv = Path("dados") / "dados_contabeis.csv"
    df_final.to_csv(destino_csv, index=False)
    logging.info(f"CSV unificado salvo em: {destino_csv}")


if __name__ == "__main__":
    try:
        baixar_arquivos()
        extrair_arquivos()
        unir_csvs()
    except Exception as e:
        logging.error(f"Processo interrompido: {e}")
        sys.exit(1)
