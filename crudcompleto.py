import mysql.connector
from prettytable import PrettyTable

def abrebanco():
    try:
        global conexao
        global comandosql
        conexao = mysql.connector.connect(host="localhost", database="univap", user="root", password="tele")
        if conexao.is_connected():
            informacoesdobanco = conexao.get_server_info()
            print(f"informacoes do banco {informacoesdobanco}")
            print("conectado!")
            comandosql = conexao.cursor()
            comandosql.execute("SELECT database()")
            nomebanco = comandosql.fetchone()
            print(f"nome fo banco {nomebanco}")
        else:
            print("banco de dados fechado!")

    except Exception as erro:
        print(f"erro ocorrido {erro}")


def mostartoda():
    grid = PrettyTable(["cod disciplina", "nome disciplina"])

    try:
        #conexao = mysql.connector.connect(host="localhost", database="univap", user="root", password="tele")
        if conexao.is_connected():
            informacoesdobanco = conexao.get_server_info()
            print(f"informacoes do banco {informacoesdobanco}")
            print("conectado!")
            comandosql = conexao.cursor()
            # cd = int(input("codigo da diciplina : "))
            # teste = (f"insert into univap.diciplinas (codigodisc,nomedisc values ({cd},'{nd}')")
            # print(teste)
            comandosql.execute(f" select * from univap.diciplinas ")
            tabela = comandosql.fetchall()
            if comandosql.rowcount > 0:
                for registro in tabela:
                    # print(f" nome da diciplina : {registro[1]}")
                    grid.add_row([registro[0], registro[1]])
            print("consulta realizada com sucesso!")
            print(grid)
            comandosql.close()
            #conexao.close()

        else:
            print("banco de dados fechado!")

    except Exception as erro:
        print(f"erro ocorrido {erro}")

def consultardiciplina():
    try:
        #conexao = mysql.connector.connect(host="localhost", database="univap", user="root", password="tele")
        if conexao.is_connected():
            informacoesdobanco = conexao.get_server_info()
            print(f"informacoes do banco {informacoesdobanco}")
            print("conectado!")
            comandosql = conexao.cursor()
            cd = int(input("codigo da diciplina : "))
            # teste = (f"insert into univap.diciplinas (codigodisc,nomedisc values ({cd},'{nd}')")
            # print(teste)
            comandosql.execute(f" select * from univap.diciplinas where codigodisc =  ({cd})")
            tabela = comandosql.fetchall()
            if comandosql.rowcount > 0:
                for registro in tabela:
                    print(f" nome da diciplina : {registro[1]}")
            print("consulta realizada com sucesso!")
            comandosql.close()
            #conexao.close()

        else:
            print("banco de dados fechado!")

    except Exception as erro:
        print(f"erro ocorrido {erro}")

def cadastradisciplina():

    try:
        #conexao = mysql.connector.connect(host="localhost", database="univap", user="root", password="tele")
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
            #conexao.close()

        else:
            print("banco de dados fechado!")

    except Exception as erro:
        print(f"erro ocorrido {erro}")
def alterardisciplina():
    try:
        #conexao = mysql.connector.connect(host="localhost", database="univap", user="root", password="tele")
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
           # conexao.close()

        else:
            print("banco de dados fechado!")

    except Exception as erro:
        print(f"erro ocorrido {erro}")

def excluirdisciplina():
    try:
        #conexao = mysql.connector.connect(host="localhost", database="univap", user="root", password="tele")
        if conexao.is_connected():
            informacoesdobanco = conexao.get_server_info()
            print(f"informacoes do banco {informacoesdobanco}")
            print("conectado!")
            comandosql = conexao.cursor()
            cd = int(input("codigo da diciplina : "))
            # teste = (f"insert into univap.diciplinas (codigodisc,nomedisc values ({cd},'{nd}')")
            # print(teste)
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
            #conexao.close()

        else:
            print("banco de dados fechado!")

    except Exception as erro:
        print(f"erro ocorrido {erro}")

abrebanco()
mostartoda()
consultardiciplina()
cadastradisciplina()
alterardisciplina()
excluirdisciplina()