import mysql.connector
try:
    conexao = mysql.connector.connect(host="localhost",database ="univap",user="root",password="tele")
    if conexao.is_connected():
        informacoesdobanco = conexao.get_server_info()
        print(f"informacoes do banco {informacoesdobanco}")
        print("conectado!")
        comandosql = conexao.cursor()
        cd = int(input("codigo da diciplina : "))
        nd = input("nome da diciplina  : ")
        teste = (f"insert into univap.diciplinas (codigodisc,nomedisc values ({cd},'{nd}')")
        print(teste)
        comandosql.execute(f"insert into univap.diciplinas (codigodisc,nomedisc) values ({cd},'{nd}')")
        conexao.commit()
        print("incluido com sucesso!")
        comandosql.close()
        conexao.close()

    else:
        print("banco de dados fechado!")

except Exception as erro:
    print(f"erro ocorrido {erro}")