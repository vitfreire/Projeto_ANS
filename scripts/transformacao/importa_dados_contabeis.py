from api.db import get_connection
import os
import sys
import logging
import pandas as pd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s - %(message)s')

csv_file = Path("dados") / "dados_contabeis.csv"

logging.info("Lendo dados contábeis do arquivo CSV...")
try:
    df = pd.read_csv(csv_file)
except FileNotFoundError:
    logging.error("Arquivo 'dados_contabeis.csv' não encontrado.")
    sys.exit(1)

df["registro_ans"] = pd.to_numeric(df["registro_ans"], errors="coerce")
df = df[df["registro_ans"].notnull()]
df["registro_ans"] = df["registro_ans"].astype(int)
df["competencia"] = pd.to_datetime(df["competencia"], errors="coerce").dt.date
df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
df = df.where(pd.notnull(df), None)

valores = df.values.tolist()
query = """
INSERT INTO demonstracoes_contabeis (
    registro_ans, competencia, codigo_contabil,
    conta_contabil, valor, origem_arquivo
)
VALUES (%s, %s, %s, %s, %s, %s)
"""

with get_connection() as conn:
    cursor = conn.cursor()
    cursor.executemany(query, valores)
    conn.commit()
    logging.info(f"{len(valores)} registros inseridos com sucesso.")
