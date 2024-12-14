import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL da página que contém as imagens
url = 'https://pt.slideshare.net/slideshow/use-a-cabea-pythonportuguspdf/253889683'  # Substitua pela URL desejada

# Fazendo a requisição à página
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrando todas as tags de imagem
image_elements = soup.find_all('img')

img_url = "https://image.slidesharecdn.com/useacabeapythonportugus-221030220405-2b789b74/85/Use-a-Cabeca-Python_Portugues-pdf-200-638.jpg"
img_url1 = "https://image.slidesharecdn.com/useacabeapythonportugus-221030220405-2b789b74/85/Use-a-Cabeca-Python_Portugues-pdf-"
img_url3 = "-638.jpg"
contador = 1

while contador <= 630:
    print(contador)
    contador += 1  # Incrementa o contador em 1
    img_url2 = contador
    img_url4 = img_url1 + str(img_url2) + img_url3
    print(img_url4)
    img_data = requests.get(img_url4).content
    filename = img_url4.split('/')[-1]
    with open(filename, 'wb') as handler:
        handler.write(img_data)
# Extraindo e baixando cada imagem

print(filename)
print("Imagens baixadas com sucesso!")
