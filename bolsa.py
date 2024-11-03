
import openpyxl
from openpyxl.styles import Font
from openpyxl.styles import Font, PatternFill
from openpyxl.formatting.rule import Rule
from openpyxl.styles.differential import DifferentialStyle






#IndValuation
#IndEndividamento
#IndiEficiência
#IndiRentabilidade
#IndiCrescimento
wbsaida = openpyxl.Workbook()

#cria planilhas
def criaPlanilaIndValuation(wbsaida):
    wbsaida.create_sheet('IndValuation')
    return

def criaPlanilaIndEndividamento(wbsaida):
    wbsaida.create_sheet('IndEndividamento')
    return

def criaPlahilhaIndiEficiência(wbsaida):
    wbsaida.create_sheet('IndiEficiência')
    return

def criaPlanilhaIndiRentabilidade(wbsaida):
    wbsaida.create_sheet('IndiRentabilidade')
    return
def criaPlanilaIndiCrescimento(wbsaida):
    wbsaida.create_sheet('IndiCrescimento')
    return
#cria colunas

IndValuation  =  wbsaida['IndValuation']
IndEndividamento  = wbsaida['IndEndividamento']
IndiEficiência  = wbsaida['IndiEficiência']
IndiRentabilidade =  wbsaida['IndiRentabilidade']
IndiCrescimento = wbsaida['IndiCrescimento']

def criaCelulaIndValuation(IndValuation):
    IndValuation.append(['DY', 'P/L', ' PEG Ratio','P/VP','EV/EBIT'])
    return

def criaPCelulaIndEndividamento(IndEndividamento):
    IndEndividamento.append(['Fruta', 'Quantidade', 'Preço'])
    return

def criaCelulaIndiEficiência(IndiEficiência):
    IndiEficiência.append(['Fruta', 'Quantidade', 'Preço'])
    return

def criaCelulaIndiRentabilidade(IndiRentabilidade):
    IndiRentabilidade.append(['Fruta', 'Quantidade', 'Preço'])
    return
def criaCelulaIndiCrescimento(IndiCrescimento):
    IndiCrescimento.append(['Fruta', 'Quantidade', 'Preço'])
    return