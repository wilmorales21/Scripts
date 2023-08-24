#Importando as bibliotecas necessárias
import requests
import json
import pandas as pd
from datetime import datetime

#URL da API. Lembre-se de mudar o número da estação e o periodo inicial e final da consulta
#Número da estação = 19314239
url = "https://www.snirh.gov.br/hidroweb/rest/api/documento/gerarTelemetricas?codigosEstacoes=193142390&tipoArquivo=2&periodoInicial=2023-01-01T00:00:00.000Z&periodoFinal=2023-01-03T22:00:00.000Z"

# Enviando a solicitação HTTP
resposta = requests.get(url)
acesso = resposta.json()
#print(acesso)

#Funcao para visualizar melhor os dados em json
#dados = pd.json_normalize(acesso)
#print(dados)

#Criando uma lista para armazenar os dados
lista = []

#Definindo variáveis na lista 'acesso'
item1 = acesso[0]
estacao = item1['nome']
codigo = item1['codigoEstacao']
latitude = item1['latitude']
longitude = item1['longitude']
altitude = item1['altitude']
estado = item1['nomeEstado']
municipio = item1['nomeMunicipio'] 

print("Estação:", estacao)
print("Código da Estação:", codigo)
print("Latitude:", latitude)
print("Longitude:", longitude)
print("Altitude:", altitude)
print("Estado:", estado)
print("Município:", municipio)

#Fazendo um loop para percorrer as variáveis na lista 'medicoes'
for item2 in acesso:
    for medicao in item2['medicoes']:
        chuva = medicao['horChuva']
        vazao = medicao['horVazao']        
        data_string = medicao['id']['horDataHora']
        data_objeto = datetime.strptime(data_string, '%Y-%m-%dT%H:%M:%S.%f%z')
        data_formatada = data_objeto.strftime('%Y-%m-%d %H:%M:%S')
      
        tupla = (estacao,codigo,latitude,longitude,altitude,estado,municipio,chuva,vazao,data_formatada)
        lista.append(tupla)

#Criando um novo dataframe no pandas
dados = pd.DataFrame(lista, columns=['Estação','Código','Latitude','Longitude','Altitude','Estado','Municipio','Chuva','Vazao','Data'])

#Criar uma planilha em Excel
ana_excel = 'estacao_ana.xlsx'
dados.to_excel(ana_excel, index=False)

print('OK?')

############################################################################
# RODAR:python3 api_ana.py 
############################################################################