
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

## 📂 Estrutura do Projeto

```text
projeto_ans/
├── api/                       # API Flask + Frontend Vue.js
│   ├── app.py                 # Configuração da API
│   └── frontend/              # Frontend Vue.js
│       └── node_modules/      # Pacotes do frontend (necessário)
├── dados/                     # Dados tratados (CSV)
├── downloads/                 # Arquivos brutos (PDF/CSV)
├── scripts/
│   ├── scraping.py            # Coleta de dados
│   ├── transformacao.py       # Processamento ETL
│   └── carga.py               # Inserção no MySQL
├── sql/
│   ├── ddl.sql                # Schema do banco
│   └── queries_analiticas.sql # Consultas complexas
├── tests/                     # Testes Pytest
├── requirements.txt           # Dependências Python
├── .env.example               # Template de variáveis
└── executar_projeto.py        # Orquestrador principal
```

---

## ⚙️ Pré-requisitos

- **Python** 3.10+
- **MySQL** 8.0+
- **Node.js** 16+  
  > Necessário para instalar dependências do frontend (`node_modules/` dentro de `api/frontend/`)
- Git

---

## 🛠️ Instalação & Execução

### 1. Clonar Repositório

```bash
git clone https://github.com/vitfreire/Projeto_ANS.git
cd Projeto_ANS
```

### 2. Criar Ambiente Virtual Python

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

### 3. Instalar Dependências Python

```bash
pip install -r requirements.txt
```

### 4. Instalar Dependências do Frontend

```bash
cd api/frontend/
npm install
cd ../../
```

> ⚠️ A pasta `node_modules/` será criada automaticamente dentro de `api/frontend/` e **deve ser mantida para o projeto funcionar localmente.**

---

### 5. Configurar Banco de Dados

Crie um arquivo `.env` com base em `.env.example`:

```env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=sua_senha
MYSQL_DATABASE=ans_dados
```

---

### 6. Executar Pipeline Completo

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
- Artefatos de desenvolvimento (`__pycache__/`, `node_modules/`)
- Arquivos de build e caches

---

## 📄 Licença

Distribuído sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 💻 Autora

**Vitória Freire**  
Analista de Sistemas  
[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?logo=github)](https://github.com/vitfreire)
```

---

Se quiser, posso gerar esse README como arquivo `.md` para você substituir no repositório ou já aplicar no seu projeto atual. Deseja isso?
