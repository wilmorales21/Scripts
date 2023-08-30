# Importando bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

#Lendo o arquivo de dados 
df = pd.read_csv('dados.csv', delimiter=' ',nrows=51)
#print(df)

#Definindo variáveis A e B
variavel_a = df['grupoa'] 
#print('VARIAVEL A \n', variavel_a)

variavel_b = df['grupob']
#print('VARIÁVEL B \n', variavel_b)

#---------------------------------------------------------
#PLOTANDO GRAFICO Q-Q PLOT PARA ANALISAR A NORMALIDADE DOS DADOS
# Gráfico Q-Q plot para o grupo A
plt.figure(figsize=(8, 6))
stats.probplot(variavel_a, dist='norm', plot=plt)
plt.title('Q-Q Plot - VARIAVEL A')
plt.xlabel('Quantis teóricos')
plt.ylabel('Quantis dos dados')

# Gráfico Q-Q plot para o grupo B
plt.figure(figsize=(8, 6))
stats.probplot(variavel_b, dist='norm', plot=plt)
plt.title('Q-Q Plot - VARIAVEL B')
plt.xlabel('Quantis teóricos')
plt.ylabel('Quantis dos dados')
plt.show()

#########################################################
#
# RODAR: python3 qq_plot.py
#
#########################################################
