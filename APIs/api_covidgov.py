#Importando as bibliotecas necessárias
import requests
import json
import base64
import pandas as pd
from datetime import datetime

# URL da API do OpendataSUS
url = 'https://imunizacao-es.saude.gov.br/_search'

# Credenciais de acesso
username = 'imunizacao_public'
password = 'qlto5t&7r_@+#Tlstigi'

# Codificando as credenciais para Base64
auth_str = f'{username}:{password}'
base64_auth_str = base64.b64encode(auth_str.encode()).decode()

#Escolhendo o tamanho de 10000 linhas com informacoes da API, segundo o manual do OpendataSUS
tamanho = json.dumps({
    'size':10000
})

# Criando uma sessão para lidar com o cookie
session = requests.Session()
session.headers.update({
    'Authorization': f'Basic {base64_auth_str}',
    'Content-Type': 'application/json'
})

# Enviar solicitação POST para acessar os dados
acesso = session.post(url,data=tamanho)

#Armazenando os dados em formato json em uma variavel
dados = acesso.json()

#Funcao para visualizar melhor os dados em json
covid = pd.json_normalize(dados['hits']['hits'])
#print(covid)

data_da_vacina = covid['_source.vacina_dataAplicacao']
#print(data_da_vacina)
#print(type(data_da_vacina))

#Convertendo series para string
data_str = data_da_vacina.to_string(index=False)
#print(data_str)
#print(type(data_str))

#Dividindo a string em linhas
linhas = data_str.splitlines()
#print(linhas)

#Criando lista para armazenar as datas depois de fazer a conversão
datas_formatadas = []

for i in linhas:
#Convertendo string de data para data no formato de números inteiros
  data_e_hora = datetime.strptime(i,'%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d')
  datas_formatadas.append(data_e_hora)     

#Definindo as variaveis que serão salvas num novo dataframe
data_nascimento = covid['_source.paciente_dataNascimento']
estabelecimento = covid['_source.estabelecimento_razaoSocial']
uf_estabelecimento = covid['_source.estabelecimento_uf']
uf_paciente= covid['_source.paciente_endereco_uf']
lote_vacina = covid['_source.vacina_lote']
codigo_raca_paciente = covid['_source.paciente_racaCor_codigo']
nome_estabelecimento = covid['_source.estalecimento_noFantasia']
fabricante_vacina = covid['_source.vacina_fabricante_nome']
dose_vacina = covid['_source.vacina_descricao_dose']
numero_dose_vacina = covid['_source.vacina_numDose']
genero_paciente = covid['_source.paciente_enumSexoBiologico']
idade_paciente = covid['_source.paciente_idade']
nome_vacina = covid['_source.vacina_nome']
etnia_paciente = covid['_source.paciente_racaCor_valor']
endereco_paciente = covid['_source.paciente_endereco_nmPais']
municipio_estabelecimento = covid['_source.estabelecimento_municipio_nome']
codigo_vacina = covid['_source.vacina_codigo']
datas = datas_formatadas

#Criando um novo dataframe extraindo apenas as variáveis de interesse do API do OpenDataSus
df_covid = pd.DataFrame(data={'DataNascimento':data_nascimento,'Estabelecimento':estabelecimento,'UF':uf_estabelecimento,'UFPaciente':uf_paciente,'LoteVacina':lote_vacina,'CodigoEtniaPaciente':codigo_raca_paciente,'NomeEstabelecimento':nome_estabelecimento,'FabricanteVacina':fabricante_vacina,'DoseVacina':dose_vacina,'NumeroDose':numero_dose_vacina,'GeneroPaciente':genero_paciente,'IdadePaciente':idade_paciente,'NomeVacina':nome_vacina,'EtniaPaciente':etnia_paciente,'EnderecoPaciente':endereco_paciente,'Municipio':municipio_estabelecimento,'CodigoVacina':codigo_vacina,'DataAplicacao':datas})
#print(df_covid)

# Convertendo a coluna 'DataAplicacao' para o formato de data do pandas
df_covid['DataAplicacao'] = pd.to_datetime(df_covid['DataAplicacao'])
#print(df_covid)

#Filtrar os dados com as condições desejadas para um determinado municipio em um determinado período de tempo
filtro_data = df_covid['DataAplicacao'] < pd.to_datetime('2023-01-01')
filtro_municipio = df_covid['Municipio'] == 'SAO PAULO'
df_filtrado = df_covid[filtro_data & filtro_municipio]

# Criar um novo DataFrame com as colunas de interesse para serem salvas em uma planilha
colunas_interesse = ['EtniaPaciente','GeneroPaciente', 'IdadePaciente','NomeVacina','DoseVacina','NumeroDose','DataAplicacao', 'Municipio']
df_final = df_filtrado[colunas_interesse]

#Criar uma nova planilha Excel
covid_excel = 'covid_vacinacao.xlsx'
writer = pd.ExcelWriter(covid_excel, engine='openpyxl')

#Escrevendo os dados na planilha Excel em colunas distintas
df_final.to_excel(writer, sheet_name='Vacinacao', index=False)

# Salvar a planilha Excel
writer.save()
print('Concluiu?')

############################################################################
#
# RODAR:python3 api_covidgov.py 
#
############################################################################
