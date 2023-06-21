import mysql.connector
try:
    conexao = mysql.connector.connect(host="localhost",database ="univap",user="root",password="tele")
    if conexao.is_connected():
        informacoesdobanco = conexao.get_server_info()
        print(f"informacoes do banco {informacoesdobanco}")
        print("conectado!")
        comandosql = conexao.cursor()
        comandosql.execute("SELECT database()")
        nomebanco = comandosql.fetchone()
        print(f"nome fo banco {nomebanco}")
    else:
        print("faha")

except Exception as erro:
    print(f"erro ocorrido {erro}")