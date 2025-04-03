import logging
import requests
from pathlib import Path

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s - %(message)s')


def baixar_arquivo(url, caminho):
    caminho = Path(caminho)
    logging.info(f"Iniciando download de {url}...")
    try:
        r = requests.get(url)
        r.raise_for_status()
        caminho.parent.mkdir(parents=True, exist_ok=True)
        with caminho.open('wb') as f:
            f.write(r.content)
        logging.info(f"Arquivo salvo em {caminho}")
    except Exception as e:
        logging.error(f"Erro ao baixar {url}: {e}")
        raise
