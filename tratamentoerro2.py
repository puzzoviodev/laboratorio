while True:
    try:
        n=int(input("digite um numerador : "))
        d=int(input("digite um denominador  : "))
        resultado = n/d
    except (ZeroDivisionError):
        print("divisão por zero")
    except Exception as erro:
        print(f"erro ocorrido {erro}")
    else:
        print(f"resultado {resultado}")
    finally:
        if input("deseja continuar ? s ou n  ") !="s":
            break

