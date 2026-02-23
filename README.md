# 📈 Gerenciador de Ações B3 - CRUD Python PostgreSQL

## 📋 Descrição do Projeto

Um sistema completo de **CRUD** (Create, Read, Update, Delete) desenvolvido em **Python** para gerenciar informações de ações da **B3** (Bolsa de Valores Brasil) utilizando **PostgreSQL** como banco de dados.

Este projeto permite inserir, consultar, atualizar e deletar dados de ações da bolsa de forma simples e direta, com uma estrutura modular e fácil de expandir.

---

## ✨ Funcionalidades

- ✅ **CREATE** - Inserir novas ações no banco de dados
- ✅ **READ** - Consultar todas as ações cadastradas
- ✅ **UPDATE** - Atualizar preços de ações
- ✅ **DELETE** - Remover ações do banco
- 🔐 Conexão segura com PostgreSQL
- 📦 Estrutura modular e reutilizável
- 🛡️ Suporte a variáveis de ambiente

---

### Pré-requisitos 🛠️

- **Python**: versão 3.7+
- **PostgreSQL**: versão 9.6+
- **pip**: gerenciador de pacotes Python

### Verificar Instalação

```bash
python --version
psql --version
```

---

## 📦 Dependências

As dependências do projeto estão listadas em `requirements.txt`:

```
psycopg2==2.9.10
psycopg2-binary==2.9.10
python-dotenv
```

---

## 🚀 Instalação e Configuração

### 1️⃣ Clonar ou Baixar o Projeto

```bash
cd /Users/hugorodrigues/Desenvolvimento/CrudPythonPostgresql
```

### 2️⃣ Criar um Ambiente Virtual (Recomendado)

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# No macOS/Linux:
source venv/bin/activate

# No Windows:
venv\Scripts\activate
```

### 3️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar Banco de Dados

#### Criar Database no PostgreSQL

```sql
-- Conectar ao PostgreSQL
psql -U postgres

-- Criar banco de dados
CREATE DATABASE acoes;

-- Conectar ao novo banco
\c acoes

-- Criar tabela de ações
CREATE TABLE acoes_b3 (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(10) NOT NULL,
    nome_empresa VARCHAR(100) NOT NULL,
    setor VARCHAR(50) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    data_cotacao DATE NOT NULL
);
```

### 5️⃣ Configurar Variáveis de Ambiente

Criar arquivo `.env` na raiz do projeto:

```env
password=sua_senha_postgres
```

⚠️ **IMPORTANTE**: Adicione `.env` ao `.gitignore` para não compartilhar credenciais:

```bash
echo ".env" >> .gitignore
```

---

## 📁 Estrutura do Projeto

```
CrudPythonPostgresql/
│
├── crud.py              # Operações CRUD (Create, Read, Update, Delete)
├── database.py          # Gerenciamento de conexão com PostgreSQL
├── requirements.txt     # Dependências do projeto
├── .env                 # Variáveis de ambiente (não commitare)
├── .gitignore           # Arquivos ignorados pelo Git
└── README.md            # Este arquivo
```

### Descrição dos Arquivos

#### `database.py`

Responsável por:

- Estabelecer conexão com PostgreSQL
- Encerrar conexão de forma segura
- Carregar variáveis de ambiente

```python
def conecta()              # Conecta ao banco de dados
def encerra_conexao(conn) # Fecha a conexão
```

#### `crud.py`

Contém as operações principais:

- `insert_acoes()` - Inserir nova ação
- `seleciona()` - Listar todas as ações
- `atualiza()` - Atualizar preço de ação
- `deleta()` - Deletar uma ação

---

## 💻 Como Usar

### Executar o Projeto

```bash
python crud.py
```

### Exemplo de Uso

Descomente as linhas de teste no arquivo `crud.py`:

```python
# Inserir uma nova ação
insert_acoes('ITSA4', 'Itaúsa', 'Holding', 10.01, '2025-09-22')

# Listar todas as ações
seleciona()

# Atualizar preço
atualiza(12.20, 'CMIG4')

# Deletar uma ação
deleta('ITSA4')
```

---

## 🔄 Operações CRUD Detalhadas

### CREATE - Inserir Dados

```python
insert_acoes(ticker, nome_empresa, setor, preco, data_cotacao)

# Exemplo:
insert_acoes('VALE3', 'Vale S.A.', 'Mineração', 22.50, '2025-02-22')
```

**Parâmetros:**

- `ticker`: código da ação (ex: VALE3)
- `nome_empresa`: nome completo da empresa
- `setor`: setor da bolsa (Mineração, Financeiro, etc)
- `preco`: valor atual da ação
- `data_cotacao`: data da cotação (formato YYYY-MM-DD)

### READ - Consultar Dados

```python
seleciona()
```

Retorna todas as ações cadastradas no formato:

```
(ticker, nome_empresa, setor, preco, data_cotacao)
```

### UPDATE - Atualizar Dados

```python
atualiza(novo_preco, ticker)

# Exemplo:
atualiza(25.75, 'VALE3')
```

### DELETE - Deletar Dados

```python
deleta(ticker)

# Exemplo:
deleta('VALE3')
```

---

## 🔐 Segurança

⚠️ **Boas Práticas Implementadas:**

1. ✅ Variáveis de ambiente para credenciais
2. ✅ Conexão segura com tratamento de erros
3. ✅ Fechamento apropriado de conexões

### Melhorias Recomendadas

Para produção, considere:

- [ ] Usar **ORM** como SQLAlchemy
- [ ] Implementar **prepared statements** para evitar SQL Injection
- [ ] Adicionar **autenticação** e **autorização**
- [ ] Usar **pool de conexões**
- [ ] Implementar **logging** detalhado
- [ ] Adicionar **testes unitários**

---

## 📊 Estrutura da Tabela

```sql
CREATE TABLE acoes_b3 (
    id SERIAL PRIMARY KEY,           -- ID único da ação
    ticker VARCHAR(10) NOT NULL,     -- Código da ação
    nome_empresa VARCHAR(100) NOT NULL, -- Nome da empresa
    setor VARCHAR(50) NOT NULL,      -- Setor da bolsa
    preco DECIMAL(10, 2) NOT NULL,   -- Preço atual
    data_cotacao DATE NOT NULL       -- Data da cotação
);
```

---

## 🐛 Troubleshooting

### Erro: "connection refused"

**Solução:**

- Verificar se PostgreSQL está rodando
- Confirmar host e porta no `database.py`

```bash
# macOS com Homebrew
brew services start postgresql

# ou iniciar manualmente
postgres -D /usr/local/var/postgres
```

### Erro: "permission denied"

**Solução:**

- Verificar usuário PostgreSQL
- Confirmar senha no arquivo `.env`

### Erro: "database does not exist"

**Solução:**

- Criar database conforme instruções acima
- Verificar nome do banco em `database.py`

### Módulo psycopg2 não encontrado

**Solução:**

```bash
pip install psycopg2-binary
# ou
pip install -r requirements.txt
```

---

## 📝 Próximas Melhorias

- [ ] Adicionar validação de dados
- [ ] Implementar API REST com Flask
- [ ] Criar interface web com HTML/CSS
- [ ] Adicionar paginação nas consultas
- [ ] Implementar testes automatizados
- [ ] Dockerizar a aplicação

---

## 📄 Licença

Este projeto é de código aberto e pode ser utilizado livremente.

---

## ✉️ Suporte

Para dúvidas ou sugestões, revise a documentação ou os comentários no código.

---

## 📅 Última Atualização

**22 de fevereiro de 2026**

---

**Desenvolvido com ❤️ usando Python e PostgreSQL**
