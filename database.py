import psycopg2
import os
from dotenv import load_dotenv
from psycopg2 import Error

load_dotenv()

password = os.getenv('password')
# def para fazer a conexão
def conecta():
    try:
        conn = psycopg2.connect(
            user="postgres",
            password="",
            host="localhost",
            port="5435",
            database="acoes",
        )
        print ("Conectado com sucesso!")

        return conn
    
    except Error as e:
        print(f"Ocorreu um erro ao tentar conectar com o banco de dados {e}")

def encerra_conexao(conn):
    if conn:
        conn.close()
    print('Conexão encerrada com sucesso!')