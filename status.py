import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Instalando o driver
servico = Service(ChromeDriverManager().install())

# Abrindo o navegador
navegador = webdriver.Chrome(service=servico)

lista_fii = ["mxrf11", "tgar11", "ggrc11", "recr11", 'rect11', 'vino11', 'brcr11', 'pvbi11', 'visc11', 'hsml11',
             'mfii11']

lista_indicadores_fii = []
for fii in lista_fii:

    # Criando url
    url = f"https://statusinvest.com.br/fundos-imobiliarios/{fii}"

    try:
        # Abrindo o navegador
        navegador.get(url)

        time.sleep(0.25)

        # Coletando infos
        segmento = navegador.find_element(By.XPATH,
                                          '//*[@id="fund-section"]/div/div/div[4]/div/div[1]/div/div/div/a/strong').text
        tipo_anbima = navegador.find_element(By.XPATH,
                                             '//*[@id="fund-section"]/div/div/div[2]/div/div[5]/div/div/div/strong').text
        valor_atual = navegador.find_element(By.XPATH, '//*[@id="main-2"]/div[2]/div[1]/div[1]/div/div[1]/strong').text
        variacao_valor_atual = navegador.find_element(By.XPATH,
                                                      '//*[@id="main-2"]/div[2]/div[1]/div[1]/div/div[2]/span/b').text
        dividend_yield = navegador.find_element(By.XPATH,
                                                '//*[@id="main-2"]/div[2]/div[1]/div[4]/div/div[1]/strong').text
        pvp = navegador.find_element(By.XPATH, '//*[@id="main-2"]/div[2]/div[5]/div/div[2]/div/div[1]/strong').text
        caixa = navegador.find_element(By.XPATH, '//*[@id="main-2"]/div[2]/div[5]/div/div[3]/div/div[1]/strong').text
        cnpj_fii = navegador.find_element(By.XPATH,
                                          '//*[@id="fund-section"]/div/div/div[2]/div/div[1]/div/div/strong').text
        administrador = navegador.find_element(By.XPATH,
                                               '//*[@id="fund-section"]/div/div/div[3]/div/div[2]/div[1]/div/strong').text
        cnpj_administrador = navegador.find_element(By.XPATH,
                                                    '//*[@id="fund-section"]/div/div/div[3]/div/div[2]/div[1]/div/span').text

        # Criando dict
        dicionario = {"fii": fii,
                      "segmento": segmento,
                      "tipo_anbima": tipo_anbima,
                      "valor_atual": valor_atual,
                      "variacao_valor_atual": variacao_valor_atual,
                      "dividend_yield": dividend_yield,
                      "pvp": pvp,
                      "caixa": caixa,
                      "cnpj_fii": cnpj_fii,
                      "administrador": administrador,
                      "cnpj_administrador": cnpj_administrador

                      }

        # Criando lista de dicts
        lista_indicadores_fii.append(dicionario)
    except Exception as e:
        print(e)

# Fecha o navegador
navegador.quit()

df = pd.DataFrame.from_dict(lista_indicadores_fii)

df.to_excel("fiis.xlsx", index=False)

