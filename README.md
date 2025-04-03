
# 📊 Projeto ANS - Sistema de Gestão de Dados de Saúde Suplementar

**Visão Geral**  
Sistema completo para coleta, transformação, armazenamento e disponibilização de dados da Agência Nacional de Saúde Suplementar (ANS). Combina técnicas modernas de engenharia de dados com desenvolvimento full-stack.

![GitHub](https://img.shields.io/badge/Python-3.10%2B-blue)
![GitHub](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Funcionalidades Principais

- **Web Scraping Automatizado**
  - Download de arquivos PDF e CSV direto do portal ANS
  - Compactação inteligente de documentos
- **Pipeline ETL Avançado**
  - Extração de dados estruturados de PDFs
  - Normalização de siglas e padrões
  - Transformação para formato relacional
- **Persistência de Dados**
  - Criação automatizada de schema MySQL
  - Carga incremental de dados
- **API RESTful**
  - Endpoints para busca textual
  - Integração CORS para acesso cross-domain
- **Interface Web Moderna**
  - Frontend em Vue.js com Vite
  - Consultas públicas via navegador
- **Suite de Testes**
  - Validação de integridade de dados
  - Testes de conexão com banco

---

## 📂 Estrutura Completa do Projeto

```text
projeto_ans/
├── .env                      # Arquivo de variáveis (NÃO versionar)
├── .pytest_cache/            # Cache de testes Pytest
│   └── v/
├── api/
│   ├── __pycache__/
│   ├── .pytest_cache/
│   ├── __init__.py
│   ├── db.py
│   ├── main.py
│   ├── package-lock.json
│   └── frontend-operadoras/  # Frontend Vue.js
│       └── node_modules/
├── dados/
│   ├── __init__.py
│   ├── dados_contabeis.csv
│   ├── cadop/
│   ├── csvs/
│   └── zips/
├── downloads/
│   ├── Anexo1.pdf
│   ├── Anexo2.pdf
│   ├── rol_procedimentos.csv
│   ├── anexos_ans.zip
│   └── Teste_Vitória_Freire.zip
├── postman/
│   ├── __init__.py
│   └── postman_collection_operadoras.json
├── scripts/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── carga_banco/
│   ├── scraping/
│   ├── transformacao/
│   └── utilitarios/
├── sql/
│   ├── __init__.py
│   ├── analise/
│   ├── ddl/
│   └── queries_analise.sql
├── tests/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── test_csvs.py
│   └── test_db.py
├── venv/                     # Ambiente virtual (NÃO versionar)
│   ├── bin/
│   ├── include/
│   ├── lib/
│   ├── pyvenv.cfg
│   └── .gitignore
├── executar_projeto.py       # Script principal
├── package-lock.json
├── package.json
├── requirements.txt
```

---

## ⚙️ Pré-requisitos

- Python 3.10+
- MySQL 8.0+
- Node.js 16+  
  > Necessário para instalar dependências do frontend (`node_modules/` dentro de `api/frontend-operadoras/`)
- Git

---

## 🛠️ Instalação & Execução

### 1. Clonar o Repositório

```bash
git clone https://github.com/vitfreire/Projeto_ANS.git
cd Projeto_ANS
```

### 2. Criar o Ambiente Virtual

```bash
python -m venv venv
```

### 3. Ativar o Ambiente Virtual

```bash
# Windows:
venv\Scripts\activate

# Linux/macOS:
source venv/bin/activate
```

### 4. Instalar Dependências do Backend

```bash
pip install -r requirements.txt
```

### 5. Instalar Dependências do Frontend

```bash
cd api/frontend-operadoras/
npm install
cd ../../
```

> ⚠️ A pasta `node_modules/` será criada automaticamente dentro de `api/frontend-operadoras/` e **deve ser mantida para o frontend funcionar localmente.**

---

### 6. Configurar Banco de Dados

Crie um arquivo `.env` com base em `.env.example`:

```env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD='sua_senha_do_Mysql'
MYSQL_DATABASE=ans_dados
```

---

### 7. Executar o Pipeline Completo

```bash
python executar_projeto.py
```

---

## 🧪 Testes Automatizados

```bash
pytest tests/ -v
```

---

## 🔍 Acesso à API

**Endpoint Principal:**
```http
GET http://localhost:5000/buscar?termo={termo_busca}
```

**Exemplo com cURL:**
```bash
curl -X GET "http://localhost:5000/buscar?termo=Unimed"
```

---

## 🌐 Frontend Web

Após iniciar a API, acesse a interface Vue.js:

```
http://localhost:5173
```

---

## 🛠️ Tecnologias Utilizadas

| Categoria          | Tecnologias                            |
|--------------------|-----------------------------------------|
| **Backend**        | Python, Flask, MySQL                    |
| **Data Processing**| Pandas, Tabula-py, BeautifulSoup        |
| **Frontend**       | Vue.js 3, Vite, Axios                   |
| **DevOps/Testes**  | Git, Pytest, dotenv                     |

---

## ⚠️ Arquivos Ignorados

O sistema ignora automaticamente:

- Credenciais (`.env`)
- Dados gerados (`*.csv`, `*.pdf`, `downloads/`, `dados/`)
- Ambientes virtuais (`venv/`)
- Caches de testes (`.pytest_cache/`, `__pycache__/`)
- Pacotes do frontend (`node_modules/`)

---

## 📄 Licença

Distribuído sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 💻 Autora

**Vitória Freire**  
Analista de Sistemas  
[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?logo=github)](https://github.com/vitfreire)
```

