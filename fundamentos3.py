import requests

from bs4 import BeautifulSoup

import warnings

from rotina3 import teste

warnings.filterwarnings('ignore')


#url do site que será feita a coleta dos dados
url = 'https://fundamentus.com.br/detalhes.php?papel=DASA3&interface=classic&interface=mobile'

#simulação de conexão comum evitando que sistema do site entenda que é um bot bloqueando o acesso
headers = {
    'User-Agent'      : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language' : 'en-US,en;q=0.5',
    'DNT'             : '1',
    'Connection'      : 'close'
}

#requisição no site
data = requests.get(url, headers=headers, timeout=6).text

#coletando o html
soup = BeautifulSoup(data, "html.parser")

#atribuindo a variável tabela
#tabela = soup.find('table')
ticket_symbol = soup.find('h1', {'class': 'acao-papel'}).text
company_name = soup.find('span', {'class': 'acao-nome'}).text
frame_cotacao = soup.find('div', {'class': 'frame-cotacao'})


information = frame_cotacao.find_all('div', {'class': 'data'})

teste6 =information[0].find('span', {'class': 'data-value'}).text
print('teste6' + str(teste6))
print('ticket_symbol'  + ticket_symbol)
print('company'  + company_name)
print('frame ' + str(frame_cotacao))



market_valuation_title = soup.find('span', {'class': 'data-title'}).text
market_valuation_tooltip = soup.find('span', {'class': 'data-tooltip'})['title']
market_valuation_value = soup.find('span', {'class': 'data-value'}).text
print(('market') + market_valuation_title )
print('tool tip' + market_valuation_tooltip)
print('value' + market_valuation_value)



#market_valuation_tooltip = self.__processing_data_tooltip(information[0])
#market_valuation_value = self.__processing_data_value(information[0])
#information = frame_cotacao.find_all('div', {'class': 'data'})
#criando o Data Frame

def teste(BeautifulSoup):
    """Process data title information.

    :param soup (bs): BeautifulSoup object.
    :return (str): String with the processed information.
    """

    return soup.find('span', {'class': 'data-title'}).text


