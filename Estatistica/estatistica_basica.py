# Importando bibliotecas
import pandas as pd
import math

#Lendo o arquivo de dados 
df = pd.read_csv('dados.csv', delimiter=' ',nrows=51)
#print(df)

#Definindo variáveis A e B
variavel_a = df['grupoa'] 
print('VARIAVEL A = ', variavel_a)

variavel_b = df['grupob']
print('VARIÁVEL B  = ', variavel_b)


#Calculando a média da variável A 
media_a = sum(variavel_a)/len(variavel_a)
print('MÉDIA DA VARIÁVEL A = ', media_a)

#Calculando a média da variável B
media_b = sum(variavel_b)/len(variavel_b)
print('MÉDIA DA VARIÁVEL B = ', media_b)

#Calculando a variância da variável A
variancia_a = sum((x - media_a)**2 for x in variavel_a) / len(variavel_a)
print('VARIANCIA EM A = ', variancia_a)

#Calculando a variância da variável B
variancia_b = sum((y - media_b)**2 for y in variavel_b) / len(variavel_b)
print('VARIANCIA EM B = ',variancia_b)

#Calculando o desvio-padrão na variável A
desvio_padrao_a = math.sqrt(variancia_a)
print('DESVIO-PADRÃO EM A = ',desvio_padrao_a)

#Calculando o desvio-padrão na variável B
desvio_padrao_b = math.sqrt(variancia_b)
print('DESVIO-PADRÃO EM B = ',desvio_padrao_b)

#Calculando a covariância entre as variáveis
covariancia_a_b = sum((x - media_a)*(y - media_b) for x,y in zip(variavel_a, variavel_b)) / len(variavel_a)
print('COVARIANCIA ENTRE A e B = ',covariancia_a_b)

#########################################################
#
# RODAR: python3 estatistica_basica.py
#
#########################################################

