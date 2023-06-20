
def soma():
    res = a+b
    print(f" resultado da soma de a + b : {res}")
def linha():

    print(" ******************** "*20)

linha()
while True:
    linha()
    a=int(input("entre com o primeiro numero :"))
    b = int(input("entre com o segundo numero :"))
    linha()
    soma()
    if input( "desenja comtinuar ? s/n") == "n":
        break

linha()

