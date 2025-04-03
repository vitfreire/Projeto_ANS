import logging
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
from pathlib import Path

# Configuração do logging
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s - %(message)s')


def fetch_pdf_links(url: str) -> list:
    """
    Acessa a página da ANS e retorna os links dos PDFs dos anexos.
    """
    logging.info("Acessando a página da ANS...")
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Erro ao acessar a página: {e}")
        raise

    soup = BeautifulSoup(response.content, 'html.parser')
    pdf_links = [
        link['href'] for link in soup.find_all('a', href=True)
        if "anexo" in link['href'].lower() and link['href'].endswith(".pdf")
    ]
    # Filtrar Anexo I e II (os dois primeiros)
    return pdf_links[:2]


def download_files(urls: list, download_dir: Path) -> list:
    """
    Baixa os arquivos PDF e retorna os caminhos dos arquivos baixados.
    """
    pdf_paths = []
    for i, url in enumerate(urls, start=1):
        full_url = url if url.startswith(
            "http") else f"https://www.gov.br{url}"
        filename = f"Anexo{i}.pdf"
        filepath = download_dir / filename
        logging.info(f"Baixando {filename}...")
        try:
            file_data = requests.get(full_url)
            file_data.raise_for_status()
            filepath.write_bytes(file_data.content)
            pdf_paths.append(filepath)
        except requests.RequestException as e:
            logging.error(f"Erro ao baixar {full_url}: {e}")
            continue
    return pdf_paths


def create_zip(file_paths: list, zip_path: Path):
    """
    Compacta os arquivos em um único arquivo ZIP.
    """
    try:
        with ZipFile(zip_path, 'w') as zipf:
            for path in file_paths:
                zipf.write(str(path), path.name)
        logging.info(f"Anexos compactados em: {zip_path}")
    except Exception as e:
        logging.error(f"Erro ao criar o arquivo ZIP: {e}")
        raise


def main():
    URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    download_dir = Path("downloads")
    download_dir.mkdir(exist_ok=True)

    try:
        anexos = fetch_pdf_links(URL)
        logging.info(f"PDFs encontrados: {anexos}")
        pdf_paths = download_files(anexos, download_dir)
        zip_path = download_dir / "anexos_ans.zip"
        create_zip(pdf_paths, zip_path)
    except Exception as e:
        logging.error(f"Erro no processo de web scraping: {e}")


if __name__ == "__main__":
    main()
