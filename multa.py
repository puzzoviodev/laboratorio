velocidade = float(input("digite a velocidade : "))

if velocidade <= 80:
    print("velocidade OK")
elif velocidade > 80:
    print("velocidade alta, voce sera multado")
    qtdmulta    = velocidade - 80.0
    valordamulta = 7.0 * qtdmulta
    print(qtdmulta)
    print((valordamulta))
    print("voce pagara a multa de {:.2f}".format(valordamulta))
print("fim do programa")
