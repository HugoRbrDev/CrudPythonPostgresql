from database import conecta, encerra_conexao

def main():

    connection = conecta()
    cursor = connection.cursor()

    #vamos fazer o Create, usando o comando Insert
    def insert_acoes(ticker, nome_empresa, setor, preco, data_cotacao):
        cmd_insert = "INSERT INTO acoes_b3 (ticker, nome_empresa, setor, preco, data_cotacao) VALUES (%s, %s, %s, %s, %s ); "
        values = ticker, nome_empresa, setor, preco, data_cotacao
        cursor.execute(cmd_insert, values)
        connection.commit()
        print('Dados Inseridos com Sucesso!')

    # Read
    def seleciona():
        cmd_select = "SELECT ticker, nome_empresa, setor, preco, data_cotacao FROM acoes_b3;"
        cursor.execute(cmd_select)
        acoes = cursor.fetchall()
        for acao in acoes:
            print (acao)
        return acao
    
    #Update
    def atualiza(novo_preco, ticker):
        cmd_update = f"UPDATE acoes_b3 SET preco={novo_preco} WHERE ticker='{ticker}'"
        cursor.execute(cmd_update)
        connection.commit()

    #Delete
    def deleta(ticker):
        cmd_delete = f"DELETE FROM acoes_b3 WHERE ticker = '{ticker}'"
        cursor.execute(cmd_delete)
        connection.commit()
        print('Registro deletado com sucesso!')

# Comandos para interação com o banco de dados
    # insert_acoes('ItausaSA', 'ITSA4', 'Holding', 10.01, '2025-09-22')
    # seleciona()
    # atualiza(12.20, 'CMIG4')
    # deleta('ItausaSA')

    encerra_conexao(connection)

if __name__ == "__main__":
    main()