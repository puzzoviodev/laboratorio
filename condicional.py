import random
x = int(random.randint(0,5))
n = int(input("digite um numero de 0 a 5   : "))

if n==x:
    print("acertou")
else:
    print("errou")

print("numero sorteado {}".format(x))

