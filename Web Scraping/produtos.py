# Código para buscar produtos a partir do preço no site Shopee
import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_precos = []

url_base = 'https://lista.mercadolivre.com.br/'
nome_produto = input('Qual o produto?')

#Fazer a requisição no site
resposta = requests.get(url_base + nome_produto)
#print(resposta.text)

site = BeautifulSoup(resposta.text,'html.parser')
#print(site.prettify())

#Pesquisar todos os produtos
produtos = site.findAll('div',attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default'})
#print(produto.prettify())

for produto in produtos:
# Pegando somente o titulo do produto
    titulo = produto.find('h2', attrs={'class':'ui-search-item__title shops__item-title'}) 
# Pegando o link do produto
    link = produto.find('a',attrs={'class':'ui-search-link'})
    real = produto.find('span',attrs={'price-tag-fraction'})
    centavos = produto.find('span',attrs={'price-tag-cents'})

    print('Titulo do Produto:\n', titulo.text)
    print('Link do Produto:\n', link['href'])

    if(centavos):
       lista_precos.append([titulo.text,link['href'],real.text + ',' + centavos.text])
    else:
       lista_precos.append([titulo.text,link['href'],real.text])
    print('\n\n')

# Criando um dataframe para armazenar os dados numa tabela
data_prices = pd.DataFrame(lista_precos,columns=['Titulo do Produto','Link','Preço do Produto'])

# Craindo um arquivo csv
#data_news.to_csv('dados_noticias.csv',index=False)

# Criando um arquivo Excel
data_prices.to_excel('precos_produtos.xlsx',index=False)








