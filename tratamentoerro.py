while True:
    try:
        n=int(input("digite um numerador : "))
        d=int(input("digite um denominador  : "))
        resultado = n/d
    except:
        print("erro ocorrido, reveja os valores")
    else:
        print(f"resultado {resultado}")
    finally:
        if input("deseja continuar ? s ou n  ") !="s":
            break

