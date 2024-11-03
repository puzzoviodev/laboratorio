import openpyxl

# Criar uma nova planilha
book = openpyxl.Workbook()
sheet = book.active

# Adicionar cabeçalhos
sheet['A1'] = 'Produto'
sheet['B1'] = 'Quantidade'
sheet['C1'] = 'Preço'

# Adicionar dados
sheet.append(['Uva', 6, 2.50])
sheet.append(['Maçã', 7, 3.00])

# Criar uma nova aba e adicionar dados nela
book.create_sheet('Frutas')
frutas_page = book['Frutas']
frutas_page.append(['Fruta', 'Quantidade', 'Preço'])

# Salvar a planilha
book.save('minha_planilha.xlsx')
