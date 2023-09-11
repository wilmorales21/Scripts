#Importando as bibliotecas necessárias
import requests
import json
import pandas as pd
from datetime import datetime

#Primeiro é preciso fazer uma requisição para verificação do número de id da estação fluviométrica a partir do código da estação
#SINTAXE DA URL: https://www.snirh.gov.br/hidroweb/rest/api/estacaotelemetrica?id={id}
#Código da estação Mario de Carvalho no município de Timóteo-MG = 56696000
url1 = 'https://www.snirh.gov.br/hidroweb/rest/api/estacaotelemetrica?id=5669600'

#Parâmetros da consulta
params1 = {
    'where': '1=1',
    'outFields': '*',
    'outSR': '4326',
    'f': 'json'
}

resposta1 = requests.get(url1,params=params1,timeout=10)
acesso1 = resposta1.json()
print('ACESSO À API DA ESTAÇÃO: \n',acesso1)

#A API da Agência Nacional das Águas(ANA) armazena o ID da estação no dicionário {'content':[{'id':id_da_estação,}]}, logo no inicio.
#Lembre-se de mudar o número da estação e o periodo inicial e final da consulta
#SINTAXE DA URL:https://www.snirh.gov.br/hidroweb/rest/api/documento/gerarTelemetricas?codigosEstacoes={codigosEstacoes}&tipoArquivo=2&periodoInicial={periodoInicial}&periodoFinal={periodoFinal}
#ID da estação = 193142390

url2 = "https://www.snirh.gov.br/hidroweb/rest/api/documento/gerarTelemetricas?codigosEstacoes=193142390&tipoArquivo=2&periodoInicial=2023-01-01T00:00:00.000Z&periodoFinal=2023-01-03T22:00:00.000Z"

# Parâmetros da consulta
params2 = {
    'where': '1=1',
    'outFields': '*',
    'outSR': '4326',
    'f': 'json'
}

# Enviando a solicitação HTTP
resposta = requests.get(url2,params=params2,timeout=10)
#resposta = requests.get(url,params=params, timeout=10)
acesso = resposta.json()
#print(acesso)

#Funcao para visualizar melhor os dados em json
#dados = pd.json_normalize(acesso)
#print(dados)

#Criando uma lista para armazenar os dados
lista = []

#Definindo variáveis na lista 'acesso'
item1 = acesso[0]
nome_estacao = item1['nome']
id_estacao= item1['id']
codigo_estacao = item1['codigoEstacao']
latitude = item1['latitude']
longitude = item1['longitude']
altitude = item1['altitude']
estado = item1['nomeEstado']
municipio = item1['nomeMunicipio'] 

print("Nome da Estação:", nome_estacao)
print('ID da Estação', id_estacao)
print("Código da Estação:", codigo_estacao)
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
      
        tupla = (nome_estacao,id_estacao,codigo_estacao,latitude,longitude,altitude,estado,municipio,chuva,vazao,data_formatada)
        lista.append(tupla)

#Criando um novo dataframe no pandas
dados = pd.DataFrame(lista, columns=['Nome Estação','ID Estação','Código Estação','Latitude','Longitude','Altitude','Estado','Municipio','Chuva','Vazao','Data'])

#Criar uma planilha em Excel
ana_excel = 'estacao_ana.xlsx'
dados.to_excel(ana_excel, index=False)

print('OK?')

############################################################################
# RODAR:python3 api_ana.py 
############################################################################
