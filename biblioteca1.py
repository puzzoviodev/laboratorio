import math
import random


num2 =random.randint(1, 10)
print(num2)
num = int(input("digite um numero  : "))

raizquadrada = math.sqrt(num)

print(f"Raiz quadrada de  {num} e   {raizquadrada} arendondado {math.ceil(raizquadrada)}")