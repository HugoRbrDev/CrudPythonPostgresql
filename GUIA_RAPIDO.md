# ⚡ Guia Rápido - CRUD B3

## 🚀 Setup em 5 Minutos

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Criar table no PostgreSQL
```sql
CREATE DATABASE acoes;
\c acoes
CREATE TABLE acoes_b3 (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(10) NOT NULL,
    nome_empresa VARCHAR(100) NOT NULL,
    setor VARCHAR(50) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    data_cotacao DATE NOT NULL
);
```

### 3. Criar arquivo `.env`
```
password=sua_senha
```

### 4. Rodar
```bash
python crud.py
```

---

## 📋 Comandos Básicos

### Inserir ação
```python
insert_acoes('PETR4', 'Petrobras', 'Energia', 28.50, '2026-02-22')
```

### Listar todas
```python
seleciona()
```

### Atualizar preço
```python
atualiza(30.00, 'PETR4')
```

### Deletar
```python
deleta('PETR4')
```

---

## 🎯 Ações Exemplo (B3)

| Ticker | Empresa | Setor |
|--------|---------|-------|
| VALE3 | Vale S.A. | Mineração |
| PETR4 | Petrobras | Energia |
| ITSA4 | Itaúsa | Holding |
| CMIG4 | Cemig | Energia |
| BBAS3 | Banco do Brasil | Financeiro |

---

## ❓ Problemas Comuns

**PostgreSQL não conecta?**
- PostgreSQL rodando? `brew services start postgresql`
- Senha correta no `.env`?
- Host/porta corretos em `database.py`?

**Módulo não encontrado?**
- `pip install psycopg2-binary`

---

**Pronto para usar!** 🎉
