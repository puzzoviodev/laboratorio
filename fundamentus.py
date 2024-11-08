import requests

from bs4 import BeautifulSoup

import warnings
warnings.filterwarnings('ignore')


#url do site que será feita a coleta dos dados
url = 'https://www.fundamentus.com.br/resultado.php'

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
tabela = soup.find('table')

#criando o Data Frame


for row in tabela.tbody.find_all('tr'): # a tag <tr>
    #buscando todas as colunas de cada linha

    columns = row.find_all('td')  # a tag <td>
    if(columns != []):
        papel = columns[0].text.strip(' ')
        segmento = columns[1].text.strip(' ')
        cotacao = columns[2].text.strip(' ')
        ffo_yield = columns[3].text.strip(' ')
        dividend_yield = columns[4].text.strip(' ')
        p_vp = columns[5].text.strip(' ')
        valor_de_mercado = columns[6].text.strip(' ')
        liquidez = columns[7].text.strip(' ')
        qtd_de_imoveis = columns[8].text.strip(' ')
        preco_do_m2 = columns[9].text.strip(' ')
        aluguel_por_m2 = columns[10].text.strip(' ')
        cap_rate = columns[11].text.strip(' ')
        vacancia_media = columns[13].text.strip(' ')
        print("papel    " + papel, 'vacancia_media    ' +  vacancia_media )
        #concatendo o Data Frame criado com as colunas que foram atribuídas a suas colunas
