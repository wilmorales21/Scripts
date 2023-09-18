#Importando as bibliotecas necessárias
import requests
import json
import pandas as pd
from datetime import datetime

#URL da API no Instituto Nacional de Meteorologia(INMET).
# Estação automática = A001
# Estação convencional = 83985
# OBS: É preciso entrar em contato com o INMET para solicitar as credenciais(TOKEN) de acesso à API.
url = 'https://apitempo.inmet.gov.br/token/estacao/2023-01-01/2023-01-02/A001/COLOQUE_SEU_TOKEN_DE_ACESSO_AQUI'

# Enviando a solicitação HTTP
resposta = requests.get(url)
acesso = resposta.json()
#print(acesso)

#dados = pd.json_normalize(acesso)
#print(dados)

################## TRABALHANDO COM ESTAÇÕES AUTOMÁTICAS ##############################
#Criando uma lista para armazenar os dados de estações automáticas
lista = []

for item in acesso:
#Definindo as variaveis na lista acesso
  estado = item['UF']
  cidade = item['DC_NOME']
  latitude = item['VL_LATITUDE']
  longitude = item['VL_LONGITUDE']
 
#Convertendo a data para o formato dataframe do pandas 
  data_string = item['DT_MEDICAO']
  data_objeto = datetime.strptime(data_string, '%Y-%m-%d')
  data_formatada = data_objeto.strftime('%Y-%m-%d')

#Convertendo a hora para o formato dataframe do pandas
  hora_string = item['HR_MEDICAO']
  hora_objeto = datetime.strptime(hora_string,'%H%M')
  hora_formatada = hora_objeto.strftime('%H:%M')
 
  estacao = item['CD_ESTACAO']
  temp_inst = item['TEM_INS']
  temp_min = item['TEM_MIN']
  temp_max = item['TEM_MAX']
  orv_inst = item['PTO_INS']
  orv_min = item['PTO_MIN']
  orv_max = item['PTO_MAX']
  ur_inst = item['UMD_INS']
  ur_min = item['UMD_MIN']
  ur_max = item['UMD_MAX']
  pres_inst = item['PRE_INS']
  pres_min = item['PRE_MIN']
  pres_max = item['PRE_MAX']
  dir_vento = item['VEN_DIR']
  vel_vento = item['VEN_VEL']
  raj_vento = item['VEN_RAJ']
  radiacao = item['RAD_GLO']
  chuva = item['CHUVA']

  tupla = (estado,cidade,latitude,longitude,data_formatada,hora_formatada,estacao,temp_inst,temp_min,temp_max,orv_inst,orv_min,orv_max,ur_inst,ur_min,ur_max,pres_inst,pres_min,pres_max,dir_vento,vel_vento,raj_vento,radiacao,chuva)
  lista.append(tupla)

dados = pd.DataFrame(lista, columns=['Estado','Cidade','Latitude','Longitude','Data','Hora','N° da Estação','Temperatura Instantânea','Temperatura Mínima','Temperatura Máxima','Orvalho Instantâneo','Orvalho Mínimo','Orvalho Máximo','UR instantânea','UR Mínima','UR Máxima','Pressão Instantânea','Pressão Mínima','Pressão Máxima','Direção do Vento','Velocidade do Vento','Rajada de Vento','Radiação','Precipitação'])

#Criar uma planilha em Excel
inmet_excel = 'estacao_inmet.xlsx'
dados.to_excel(inmet_excel, index=False)

############################ TRABALHANDO COM ESTAÇÕES CONVENCIONAIS ########################
#Criando uma lista para armazenar os dados de estações convencionais
#lista = []

#for item in acesso:
#Definindo as variaveis na lista acesso
#  estado = item['UF']
#  cidade = item['DC_NOME']
#  latitude = item['VL_LATITUDE']
#  longitude = item['VL_LONGITUDE']
 
#Convertendo a data para o formato dataframe do pandas 
#  data_string = item['DT_MEDICAO']
#  data_objeto = datetime.strptime(data_string, '%Y-%m-%d')
#  data_formatada = data_objeto.strftime('%Y-%m-%d')

#Convertendo a hora para o formato dataframe do pandas
#  hora_string = item['HR_MEDICAO']
#  hora_objeto = datetime.strptime(hora_string,'%H%M')
#  hora_formatada = hora_objeto.strftime('%H:%M')

#  estacao = item['CD_ESTACAO']
#  temp_min = item['TEMP_MIN']
#  temp_max = item['TEMP_MAX']
#  ur_horaria = item['UMID_HORA']
#  pressao = item['PRESS_EST']
#  dir_vento = item['VENT_DIR']
#  vel_vento = item['VENT_VEL']
#  nebulosidade = item['NEBU_HORA']
#  radiacao = item['INSO_HORA']
#  chuva = item['CHUVA']

#  tupla = (estado,cidade,latitude,longitude,data_formatada,hora_formatada,estacao,temp_min,temp_max,ur_horaria,pressao,dir_vento,vel_vento,nebulosidade,radiacao,chuva)
#  lista.append(tupla)

#dados = pd.DataFrame(lista, columns=['Estado','Cidade','Latitude','Longitude','Data','Hora','N° da Estação','Temperatura Mínima','Temperatura Máxima','UR Horária','Pressão na Estação','Direção do Vento','Velocidade do Vento','Nebulosidade','Radiação','Precipitação'])

#Criar uma planilha em Excel
#inmet_excel = 'convencional.xlsx'
#dados.to_excel(inmet_excel, index=False)

print('OK?')

############################################################################
# RODAR:python3 api_inmet.py 
############################################################################
