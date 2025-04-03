import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from pathlib import Path
import os


def create_app():
    app = Flask(__name__)

    # Configuração do logging
    logging.basicConfig(level=logging.INFO,
                        format='[%(asctime)s] %(levelname)s - %(message)s')

    # Configuração do CORS para todas as origens
    CORS(app, supports_credentials=True)

    # Obtém o caminho do CSV via variável de ambiente ou usa o padrão
    csv_path = os.getenv("CSV_PATH", "dados/cadop/cadop_tratado.csv")
    csv_file = Path(csv_path)

    try:
        df_operadoras = pd.read_csv(csv_file, dtype=str, encoding="utf-8")
        logging.info(f"Arquivo {csv_path} carregado com sucesso.")
    except FileNotFoundError:
        logging.error(
            f"Arquivo não encontrado: {csv_path}. Criando DataFrame vazio.")
        df_operadoras = pd.DataFrame(columns=[
            "registro_ans", "cnpj", "razao_social", "nome_fantasia",
            "modalidade", "uf", "municipio", "data_registro"
        ])

    @app.route("/buscar", methods=["GET"])
    def buscar_operadoras():
        termo = request.args.get("q", "").strip().lower()
        if not termo:
            return jsonify([])

        # Busca de forma case-insensitive pelo termo em 'nome_fantasia'
        resultados = df_operadoras[
            df_operadoras["nome_fantasia"].str.lower(
            ).str.contains(termo, na=False)
        ].copy()
        return jsonify(resultados.head(20).to_dict(orient="records"))

    return app


if __name__ == "__main__":
    app = create_app()
    # Configurações do servidor via variáveis de ambiente
    host = os.getenv("FLASK_HOST", "localhost")
    port = int(os.getenv("FLASK_PORT", 5000))
    debug = bool(os.getenv("FLASK_DEBUG", True))
    app.run(debug=debug, host=host, port=port, use_reloader=False)
