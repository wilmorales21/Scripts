import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_news = []

#Fazer uma requisição ao site
resposta = requests.get('https://g1.globo.com')
conteudo = resposta.content

#Pegar o conteudo da requisição e converte num objeto do BeautifulSoup
site = BeautifulSoup(conteudo,'html.parser')

#Html das noticias
noticias = site.findAll('div',attrs={'class': 'feed-post-body'})
#print(noticias)
#print(type(noticias))

#Imprimir apenas os titulos e subtitulos das noticias
for news in noticias:
  titulo = news.find('a',attrs={'class': 'feed-post-link'})
#  print(titulo.text)

# Imprime o link da noticia
  print(titulo['href'])

# Verificando se a noticia tem subtitulo
  subtitulo = news.find('a',attrs={'class':'feed-post-body-resume'})
  if(subtitulo):
    lista_news.append([titulo.text,subtitulo.text,titulo['href']])
  else:
    lista_news.append([titulo.text,'',titulo['href']]) 
    print(subtitulo.text)

# Criando um dataframe para armazenar os dados numa tabela
data_news = pd.DataFrame(lista_news,columns=['Titulo','Subtitulo','Link'])

# Craindo um arquivo csv
#data_news.to_csv('dados_noticias.csv',index=False)

 Criando um arquivo Excel
data_news.to_excel('dados_noticias.xlsx',index=False)

#print(data_news)
