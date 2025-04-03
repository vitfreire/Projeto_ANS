import os
import platform
import subprocess
import threading
import time
import logging
from pathlib import Path

# Configuração do logging
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s - %(message)s')


def executar_etapas(etapas, use_shell):
    # Se o sistema for Windows, configura PYTHONPATH para a raiz do projeto
    env = os.environ.copy()
    if platform.system() == "Windows":
        env["PYTHONPATH"] = str(Path(__file__).resolve().parent)
    for descricao, script in etapas:
        logging.info(f"Executando etapa: {descricao}")
        try:
            subprocess.run(["python", script], check=True,
                           shell=use_shell, env=env)
            logging.info(f"Etapa '{descricao}' concluída com sucesso.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Erro na etapa '{descricao}': {e}")
            raise


def aguardar_arquivo(csv_path, timeout=15):
    path = Path(csv_path)
    logging.info(f"Verificando se o arquivo {csv_path} foi gerado...")
    for _ in range(timeout):
        if path.exists():
            logging.info("Arquivo encontrado, iniciando servidores...")
            return True
        logging.info(f"Aguardando arquivo: {csv_path}")
        time.sleep(1)
    logging.error(f"Timeout esperando o arquivo {csv_path}")
    return False


def iniciar_api(use_shell):
    logging.info("Iniciando API Flask...")
    try:
        subprocess.Popen(["python", "api/main.py"], shell=use_shell)
    except Exception as e:
        logging.error(f"Falha ao iniciar API: {e}")


def iniciar_frontend(use_shell):
    logging.info("Iniciando frontend Vue...")
    frontend_path = Path("api/frontend-operadoras").resolve()
    env = os.environ.copy()

    npm_executable = "npm"
    args = [npm_executable, "run", "dev"]

    # Se o sistema for Windows, tenta utilizar o npm local
    if platform.system() == "Windows":
        npm_local = frontend_path / "node_modules" / ".bin" / "npm.cmd"
        if npm_local.is_file():
            npm_executable = str(npm_local)
            args = [npm_executable, "run", "dev"]
            logging.info(f"Utilizando npm local: {npm_executable}")
        else:
            logging.warning(
                "npm.cmd não encontrado localmente. Utilizando fallback com 'npx --yes npm run dev'...")
            npm_executable = "npx"
            args = [npm_executable, "--yes", "npm", "run", "dev"]

    # Verifica a versão do npm (ou npx)
    try:
        version_result = subprocess.run(
            [npm_executable, "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=str(frontend_path),
            shell=use_shell
        )
        version = version_result.stdout.strip()
        logging.info(f"Versão do {npm_executable}: {version}")
    except Exception as e:
        logging.error(f"Erro ao obter a versão do {npm_executable}: {e}")

    try:
        subprocess.Popen(args, cwd=str(frontend_path),
                         env=env, shell=use_shell)
        logging.info("Comando 'npm run dev' iniciado com sucesso.")
    except Exception as e:
        logging.error(f"Falha ao iniciar o frontend: {e}")


def main():
    # Define use_shell conforme o sistema operacional
    use_shell = True if platform.system() == "Windows" else False

    etapas = [
        ("Criar banco e tabelas", "scripts/carga_banco/cria_banco_ans.py"),
        ("Carregar e tratar dados das operadoras ativas",
         "scripts/carga_banco/carrega_operadoras_ativas.py"),
        ("Importar operadoras ativas no banco",
         "scripts/carga_banco/importa_operadoras_mysql.py"),
        ("Carregar demonstrações contabeis",
         "scripts/carga_banco/carrega_demonst_contabeis.py"),
        ("Importar demonstrações contabeis no banco",
         "scripts/transformacao/importa_dados_contabeis.py")
    ]

    try:
        executar_etapas(etapas, use_shell)
    except Exception:
        logging.error(
            "Encerrando a execução devido a erros nas etapas anteriores.")
        exit(1)

    csv_path = "dados/cadop/cadop_tratado.csv"
    if not aguardar_arquivo(csv_path):
        exit(1)

    # Inicia os servidores em threads separadas
    frontend_thread = threading.Thread(
        target=iniciar_frontend, args=(use_shell,))
    api_thread = threading.Thread(target=iniciar_api, args=(use_shell,))

    frontend_thread.start()
    # Pequena pausa para iniciar o frontend antes da API
    time.sleep(2)
    api_thread.start()


if __name__ == '__main__':
    main()
