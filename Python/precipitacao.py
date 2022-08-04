# Importando bibliotecas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Abrindo os arquivos com os dados
df = pd.read_csv('precipitacao.csv', delimiter=' ', nrows=13)

# Conversao de uma coluna object para string
df['mes'] = df['mes'].astype('|S')

x1 = df['mes']
#print(x1)

#determinando as colunas dos anos
y1 = df['y2009']
y2 = df['y2011']
y3 = df['y2019']
y4 = df['y2020']


x = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
largura = 0.2

plt.bar(x - 0.3, y1, width = largura, color='blue', label='2009')
plt.bar(x - 0.1, y2, width = largura, color='gold',label='2011')
plt.bar(x + 0.1, y3, width = largura, color='olivedrab',label='2019')
plt.bar(x + 0.3, y4, width = largura, color='red',label='2020')

plt.title('Precipitação mensal')
plt.ylabel('Precipitação mensal (mm)')
plt.xlabel('Meses')

#plotar legenda
plt.legend(ncol=1,loc='upper left')

#Ajustando os valores no eixo x
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'])

plt.show()

#####################################################
#
# RODAR O CODIGO: python3 precipitacao.py
#
######################################################
