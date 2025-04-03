import os
import subprocess
import logging

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s - %(message)s')


def executar_etapa(descricao, comando):
    logging.info(descricao)
    try:
        subprocess.run(["python", comando], check=True)
    except subprocess.CalledProcessError:
        logging.error(f"Erro durante {descricao.lower()}")
        exit(1)


def main():
    logging.info("Iniciando execução completa do projeto ANS...")
    executar_etapa("Etapa 1: Criando banco e tabelas...", "cria_banco_ans.py")
    executar_etapa("Etapa 2: Importando operadoras...",
                   "importa_operadoras_mysql.py")
    executar_etapa("Etapa 3: Importando demonstrações contábeis...",
                   "importa_dados_contabeis.py")
    logging.info("Projeto executado com sucesso!")


if __name__ == "__main__":
    main()
