def potencia(base,expoente):
    p=1
    for cont in range(1,expoente+1,1):
        p=p*base
    print(f"resultado base {base} elavado a {expoente} =  {p}")




a=int(input("entre com a base :"))
b = int(input("entre com o exponte :"))

potencia(a,b)