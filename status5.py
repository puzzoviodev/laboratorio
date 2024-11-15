import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Configuração do WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

# URL do site Status Invest
url = 'https://statusinvest.com.br/acoes'

# Acessa a URL
driver.get(url)

# Aguarda a página carregar
time.sleep(3)

# Obtém o conteúdo HTML da página
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Encontra todos os elementos que contêm as informações das ações
acoes = soup.find_all('div', class_='ticker')

# Estrutura para armazenar os dados das ações
acoes_data = []

# Extrai os dados de interesse
for acao in acoes:
    nome = acao.find('a', class_='ticker__symbol').text.strip()
    preco = acao.find('strong', class_='ticker__price').text.strip()
    variacao = acao.find('span', class_='ticker__change').text.strip()

    acoes_data.append([nome, preco, variacao])

# Exibe os dados extraídos
for data in acoes_data:
    print(data)

# Fecha o navegador
driver.quit()
