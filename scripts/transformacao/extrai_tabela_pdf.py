import os
import logging
import pandas as pd
import zipfile
import tabula
from pathlib import Path

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s - %(message)s')
tabula.backend.encoding = 'utf-8'

pdf_path = Path("downloads") / "Anexo1.pdf"
csv_path = Path("downloads") / "rol_procedimentos.csv"
zip_path = Path("downloads") / "Teste_Vitoria_Freire.zip"

if not pdf_path.exists():
    logging.error(f"Arquivo não encontrado: {pdf_path}")
    raise FileNotFoundError(f"Arquivo não encontrado: {pdf_path}")

logging.info("Extraindo tabelas do PDF (pode demorar)...")
try:
    tables = tabula.read_pdf(str(pdf_path), pages="all",
                             multiple_tables=True, lattice=True)
    df_total = pd.concat(tables, ignore_index=True)
except Exception as e:
    logging.error(f"Erro ao extrair tabelas: {e}")
    raise

logging.info("Realizando limpeza e substituição de siglas...")
for col in df_total.columns:
    if "od" in col.lower():
        df_total[col] = df_total[col].replace("OD", "Odontologia")
    if "amb" in col.lower():
        df_total[col] = df_total[col].replace("AMB", "Ambulatorial")

df_total.columns = [col.replace('\r', ' ').strip() for col in df_total.columns]
df_total = df_total.drop(
    columns=[col for col in df_total.columns if "Unnamed" in col], errors='ignore')
df_total.replace({r'\r': ' '}, regex=True, inplace=True)

df_total.to_csv(csv_path, index=False)
logging.info(f"CSV salvo em: {csv_path}")

with zipfile.ZipFile(zip_path, 'w') as zipf:
    zipf.write(str(csv_path), csv_path.name)
logging.info(f"Arquivo compactado gerado: {zip_path}")
