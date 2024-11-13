import requests
from bs4 import BeautifulSoup

# URL do site de investimentos (exemplo)
url = 'https://statusinvest.com.br/acoes'

try:
    # Enviando uma solicitação GET para a URL
    response = requests.get(url)
    response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida

    # Parseando o conteúdo HTML da página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrando todas as ações listadas na página
    acoes = soup.find_all('div', class_='acao')

    for acao in acoes:
        nome = acao.find('a', class_='acao-titulo').text.strip()
        preco = acao.find('span', class_='acao-preco').text.strip()
        variação = acao.find('span', class_='acao-variacao').text.strip()

        print(f'Nome: {nome}\nPreço: {preco}\nVariação: {variação}\n')

except requests.exceptions.RequestException as e:
    print(f'Erro ao acessar o site: {e}')
