# 📋 Requirements e Dependências

## 📦 Arquivo `requirements.txt`

```
psycopg2==2.9.10
psycopg2-binary==2.9.10
python-dotenv>=0.19.0
```

---

## 📥 Instalar Dependências

### Opção 1: Usar requirements.txt

```bash
# Com ambiente virtual ativado
pip install -r requirements.txt
```

### Opção 2: Instalar Individualmente

```bash
pip install psycopg2-binary
pip install python-dotenv
```

### Opção 3: Instalar com Versão Específica

```bash
pip install psycopg2-binary==2.9.10
pip install python-dotenv==0.19.0
```

---

## 🔍 Verificar Instalação

```bash
# Ver pacotes instalados
pip list

# Verificar versão psycopg2
python -c "import psycopg2; print(psycopg2.__version__)"

# Verificar dotenv
python -c "import dotenv; print('dotenv OK')"
```

---

## 📚 Descrição das Dependências

### 1. **psycopg2** / **psycopg2-binary**

**O que é:**

- Adaptador PostgreSQL para Python
- Permite conexão e manipulação de dados no PostgreSQL

**Por quê:**

- Ativa o `import psycopg2` usado em `database.py`
- Comunica com o banco de dados

**Documentação:**

- [psycopg2.org](https://www.psycopg.org/)

**Alternativas:**

- `asyncpg` - versão assíncrona
- `pg8000` - alternativa pura Python
- `SQLAlchemy` - ORM completo

### 2. **python-dotenv**

**O que é:**

- Carrega variáveis de ambiente do arquivo `.env`
- Fornece `load_dotenv()` e `os.getenv()`

**Por quê:**

- Usado para carregar credenciais de forma segura
- Não expõe senhas no código

**Documentação:**

- [python-dotenv](https://github.com/theskumar/python-dotenv)

**Alternativas:**

- `environs` - parsing mais robusto
- `pydantic` - validação de variáveis

---

## 🌀 Atualizando Dependências

### Verificar Atualizações Disponíveis

```bash
pip list --outdated
```

### Atualizar um Pacote

```bash
pip install --upgrade psycopg2
pip install --upgrade psycopg2-binary
```

### Atualizar Tudo

```bash
pip install -r requirements.txt --upgrade
```

### Criar Nova Versão do requirements.txt

```bash
pip freeze > requirements.txt
```

---

## 🧪 Requirements para Desenvolvimento

### Criar `requirements-dev.txt`

```
# requirements-dev.txt
-r requirements.txt

# Testing
pytest>=7.0.0
pytest-cov>=3.0.0

# Code Quality
black>=22.0.0
flake8>=4.0.0
pylint>=2.12.0

# Type Checking
mypy>=0.910

# Documentation
sphinx>=4.5.0
```

### Instalar Dependências de Desenvolvimento

```bash
pip install -r requirements-dev.txt
```

---

## 🐍 Requisitos do Sistema

| Componente     | Versão Mínima | Recomendado |
| -------------- | ------------- | ----------- |
| **Python**     | 3.7           | 3.10+       |
| **PostgreSQL** | 9.6           | 13+         |
| **pip**        | 20.0          | 22.0+       |
| **psycopg2**   | 2.8           | 2.9+        |

---

## ✅ Checklist de Instalação

```
□ Python 3.7+ instalado
□ PostgreSQL instalado e rodando
□ Ambiente virtual criado
□ pip atualizado (pip install --upgrade pip)
□ requirements.txt instalado
□ Arquivo .env criado com credenciais
□ Banco 'acoes' criado
□ Tabela 'acoes_b3' criada
□ Conexão testada com sucesso
```

---

## 🐛 Troubleshooting de Pacotes

### Erro: `No module named 'psycopg2'`

**Solução:**

```bash
pip install psycopg2-binary
# ou
pip install psycopg2
```

### Erro: `No module named 'dotenv'`

**Solução:**

```bash
pip install python-dotenv
```

### Erro: `ImportError: DLL load failed`

**Solução (Windows):**

```bash
pip install psycopg2-binary --only-binary psycopg2-binary
```

### Erro: `Connection refused`

**Não é erro de pacote**, mas de conexão:

```bash
# Verificar se PostgreSQL está rodando
pg_isready -h localhost -p 5432
```

---

## 🔄 Ambiente Virtual

### Criar Ambiente Virtual

```bash
python -m venv venv
```

### Ativar Ambiente Virtual

**macOS/Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### Desativar Ambiente Virtual

```bash
deactivate
```

### Remover Ambiente Virtual

```bash
rm -rf venv  # macOS/Linux
rmdir venv   # Windows
```

---

## 📊 Comparação de Drivers PostgreSQL Python

| Driver           | Tipo       | Performance | Async | ORM    |
| ---------------- | ---------- | ----------- | ----- | ------ |
| **psycopg2**     | Sync       | ⭐⭐⭐⭐    | ❌    | Manual |
| **asyncpg**      | Async      | ⭐⭐⭐⭐⭐  | ✅    | Manual |
| **SQLAlchemy**   | Sync/Async | ⭐⭐⭐      | ✅    | ✅     |
| **Tortoise ORM** | Async      | ⭐⭐⭐      | ✅    | ✅     |

---

## 📝 Dicas de Performance

### 1. Use Índices no Banco

```sql
CREATE INDEX idx_ticker ON acoes_b3(ticker);
CREATE INDEX idx_setor ON acoes_b3(setor);
```

### 2. Use Executemany para Múltiplas Inserções

```python
# Lento ❌
for item in items:
    cursor.execute("INSERT INTO ... VALUES (...)", item)

# Rápido ✅
cursor.executemany("INSERT INTO ... VALUES (%s, %s)", items)
```

### 3. Use Connection Pooling

```python
from psycopg2.pool import SimpleConnectionPool
```

### 4. Limit Queries

```python
cursor.execute("SELECT * FROM acoes_b3 LIMIT 100")
```

---

## 🚀 Deployment

### Criar Build Production

```bash
# Usar requirements.txt fixo
pip freeze > requirements.txt

# Testar instalação limpa
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python crud.py
```

---

## 📚 Recursos Adicionais

- [Psycopg2 Documentation](https://www.psycopg.org/2/docs/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [Python Packaging Guide](https://packaging.python.org/)

---

**Pronto para desenvolver!** 🎯
