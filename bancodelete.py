import mysql.connector
try:
    conexao = mysql.connector.connect(host="localhost",database ="univap",user="root",password="tele")
    if conexao.is_connected():
        informacoesdobanco = conexao.get_server_info()
        print(f"informacoes do banco {informacoesdobanco}")
        print("conectado!")
        comandosql = conexao.cursor()
        cd = int(input("codigo da diciplina : "))
        #teste = (f"insert into univap.diciplinas (codigodisc,nomedisc values ({cd},'{nd}')")
        #print(teste)
        comandosql.execute(f" select * from univap.diciplinas where codigodisc =  ({cd})")
        tabela = comandosql.fetchall()
        if comandosql.rowcount > 0:
            for registro in tabela:
                print(f" nome da diciplina : {registro[1]}")
            nn = input("Entre com o reg para deletar da dicisplina : ")
            comandosql.execute(f" delete from  univap.diciplinas  where codigodisc =  {cd}")
            conexao.commit()
        print("consulta realizada com sucesso!")
        print("alteracao  realizada com sucesso!")

        comandosql.close()
        conexao.close()

    else:
        print("banco de dados fechado!")

except Exception as erro:
    print(f"erro ocorrido {erro}")