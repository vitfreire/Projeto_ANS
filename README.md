
# 📊 Projeto ANS - Sistema de Gestão de Dados de Saúde Suplementar

**Visão Geral**  
Sistema completo para coleta, transformação, armazenamento e disponibilização de dados da Agência Nacional de Saúde Suplementar (ANS). Combina técnicas modernas de engenharia de dados com desenvolvimento full-stack.

![GitHub](https://img.shields.io/badge/Python-3.10%2B-blue)
![GitHub](https://img.shields.io/badge/License-MIT-green)

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

## 📂 Estrutura do Projeto

```text
projeto_ans/
├── api/                       # API Flask + Frontend Vue.js
│   ├── app.py                 # Configuração da API
│   └── frontend/              # Componentes Vue.js
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
├── requirements.txt           # Dependências
├── .env.example               # Template de variáveis
└── executar_projeto.py        # Orquestrador principal
```

## ⚙️ Pré-requisitos

- Python 3.10+
- MySQL 8.0+
- Node.js 16+ (para frontend)
- Git

## 🛠️ Instalação & Execução

### 1. Clonar Repositório
```bash
git clone https://github.com/vitfreire/Projeto_ANS.git
cd Projeto_ANS
```

### 2. Ambiente Virtual
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar Banco de Dados
Crie `.env` baseado no template:
```env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DATABASE=ans_dados

```

### 5. Executar Pipeline Completo
```bash
python executar_projeto.py
```

## 🧪 Testes Automatizados
```bash
pytest tests/ -v
```

## 🔍 Acesso à API
**Endpoint Principal:**
```http
GET http://localhost:5000/buscar?termo={termo_busca}
```

**Exemplo com cURL:**
```bash
curl -X GET "http://localhost:5000/buscar?termo=Unimed"
```

## 🌐 Frontend Web
Após iniciar a API:
Acesse: `http://localhost:5173`

## 🛠️ Tecnologias Utilizadas

| Categoria       | Tecnologias                                  |
|-----------------|---------------------------------------------|
| **Backend**     | Python, Flask, MySQL                       |
| **Data Processing** | Pandas, Tabula-py, BeautifulSoup       |
| **Frontend**    | Vue.js 3, Vite, Axios                       |
| **DevOps**      | Git, pytest, dotenv                        |

## ⚠️ Arquivos Ignorados
O sistema automaticamente ignora:
- Credenciais (`.env`)
- Dados sensíveis (`*.csv`, `*.pdf`)
- Artefatos de desenvolvimento (`__pycache__/`, `node_modules/`)
- Logs e arquivos temporários

## 📄 Licença
Distribuído sob licença MIT. Veja [LICENSE](LICENSE) para detalhes.

## 💻 Autora
**Vitória Freire**  
[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?logo=github)](https://github.com/vitfreire)  
Analista de Sistemas | 

