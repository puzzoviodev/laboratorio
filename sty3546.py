import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from unidecode import unidecode

# Configuração do WebDriver do Selenium
options = webdriver.ChromeOptions()
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

# URL de uma ação específica no Status Invest
url = 'https://statusinvest.com.br/acoes/petr4'
driver.get(url)

# Aguarda o carregamento do conteúdo dinâmico
time.sleep(6)  # Aumenta o tempo de espera para garantir que o conteúdo seja carregado

# Obtém o HTML da página carregada
html = driver.page_source
soup = BeautifulSoup(unidecode(html), 'html.parser')

# Estrutura para armazenar os dados dos indicadores
indicadores_data = {}

# Localizando os indicadores na página
#indicadores = soup.find_all('div', class_='w-50 w-sm-33 w-md-25 w-lg-16_6 mb-2 mt-2 item')
indicadores = soup.find_all('div', class_='"card rounded text-main-green-dark')
# Extraindo os dados de interesse
for indicador in indicadores:
    try:
        nome = indicador.find('h3', class_='title').text.strip()
        valor = indicador.find('strong', class_='value').text.strip()
        indicadores_data[nome] = valor
    except AttributeError:
        continue

# Convertendo os dados para um DataFrame pandas
df = pd.DataFrame(list(indicadores_data.items()), columns=['Indicador', 'Valor'])

# Exibindo o DataFrame
print(df)

# Salvando os dados em um arquivo CSV
df.to_csv('indicadores_petr4.csv', index=False)

# Fecha o navegador
driver.quit()
