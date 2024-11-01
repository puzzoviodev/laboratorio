import openpyxl


# Crie um novo livro do Excel
workbook = openpyxl.Workbook()

# Selecione a primeira planilha
sheet = workbook.active

# Adicione alguns dados
print("1")
sheet['A1'] = 'Nome'
sheet['B1'] = 'Idade'
sheet['A2'] = 'João'
sheet['B2'] = 25
sheet['A3'] = 'Maria'
sheet['B3'] = 30
sheet['C3'] = 'silvio'

sheet['C4'] = 'silvio'
sheet['c5'] = '52'
print("2")
conta = 'c6'
sheet[conta] = 'tewste'







#= 1

#print(i)
#while i <= 100:
#    conta2 = 'c' + str(i)

#    faker = Faker()
#    nome = faker.name()
#    print(nome)
    # numero = random.randint(1, 100)
#    sheet[conta2] = nome
#    i += 1

# Salve o arquivo do Excel
workbook.save("exemplo2.xlsx")
print("55")

