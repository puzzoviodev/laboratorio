import openpyxl
from openpyxl.styles import Color, PatternFill, Font, Border
from openpyxl.formatting.rule import ColorScaleRule, CellIsRule, FormulaRule






#IndValuation
#IndEndividamento
#IndiEficiência
#IndiRentabilidade
#IndiCrescimento
#wb = openpyxl.load_workbook('statusinvest2.xlsx')
wbsaida = openpyxl.Workbook()
#ws = wbsaida.active

redFill = PatternFill(start_color='FFEE1111',
end_color='FFEE1111',
fill_type='solid')


#cria planilhas
def criaPlanilaIndValuation(wbsaida):
    wbsaida.create_sheet('IndValuation')
    IndValuation = wbsaida['IndValuation']
    IndValuation.append(['D.Y', 'P/L', ' PEG Ratio','P/VP','EV/EBITDA','EV/EBIT','P/EBITDA','P/EBIT','VPA','P/Ativo',
                         'LPA','P/SR','P/Ativo Circ. Liq.'])
    return


def criaPCelulaIndEndividamento(IndEndividamento):
    wbsaida.create_sheet('IndEndividamento')
    IndEndividamento = wbsaida['IndEndividamento']
    IndEndividamento.append(['Dív. líquida/PL', 'Dív. líquida/EBITDA', 'Dív. líquida/EBIT','PL/Ativos','Passivos/Ativos','Liq. corrente'])
    return

def criaCelulaIndiEficiência(IndiEficiência):
    wbsaida.create_sheet('IndiEficiência')
    IndiEficiência = wbsaida['IndiEficiência']
    IndiEficiência.append(['M. Bruta', 'M. EBITDA', 'M. EBIT', 'M. Líquida'])
    return

def criaCelulaIndiRentabilidade(IndiRentabilidade):
    wbsaida.create_sheet('IndiRentabilidade')
    IndiRentabilidade = wbsaida['IndiRentabilidade']
    IndiRentabilidade.append(['ROE', 'ROA', 'ROIC','Giro ativos',''])
    return
def criaCelulaIndiCrescimento(IndiCrescimento):
    wbsaida.create_sheet('IndiCrescimento')
    IndiCrescimento = wbsaida['IndiCrescimento']
    IndiCrescimento.append(['CAGR Receitas 5 anos', 'CAGR Lucros 5 anos'])
    return

def gravaCelulaIndiRentabilidade(imposto,celula):

    #values = ws.cell(row=imposto, column=1).value
    var1 = 'A' + str(imposto)
    celula[var1] = 'teste1'
    myFont = Font()
    myBorder = Border()
    celula.conditional_formatting.add('E1:E10',
                                  FormulaRule(formula=['E1=0'], font=myFont, border=myBorder, fill=redFill))
    celula['B1'] = '3.14%'
   celula['B1'].value = '0.031400000000000004'
     celula['B1'].number_format = '0%'
    return

criaPlanilaIndValuation(wbsaida)
criaPCelulaIndEndividamento(wbsaida)
criaCelulaIndiEficiência(wbsaida)
criaCelulaIndiRentabilidade(wbsaida)
criaCelulaIndiCrescimento(wbsaida)

imposto = 1
while imposto < 10:
    imposto = imposto + 1
    celula = wbsaida['IndiRentabilidade']




    gravaCelulaIndiRentabilidade(imposto,celula)

    print(imposto)

wbsaida.save("exemplo2.xlsx")
