import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Abrindo os arquivos com os dados
df = pd.read_csv('oscilacao_antartica.csv', delimiter=' ',nrows=253)

# Conversao de uma coluna object para string
df['MES'] = df['MES'].astype('|S')

x1 = df['MES']
#print(x1)

# Determinando as colunas dos anos
y1 = df['YEARS']
#print(y1)

# Plotando a curva da oscilacao antartica
y1.plot(color='grey')

# Colocando um titulo na figura
plt.title('Evolução mensal da Oscilação Antártica')

# Colocando um titulo no eixo x
plt.xlabel('Anos')

# comando para plotar uma linha horizontal no meio da figura
plt.axhline(0, color='grey', lw= 0.5, linestyle= '-')

# Ajustando o intervalo de valores no eixo y
plt.ylim([-3.0, 3.0])

# Determinando os valores no eixo y
plt.yticks([-3.0,-2.0,-1.0,0,1.0,2.0,3.0])

# Ajustando os valores no eixo x
#plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'])
plt.xticks([0,24,48,72,96,120,144,168,192,216,240],['2000','2002','2004','2006','2008','2010','2012','2014','2016','2018','2020'])

# Ajustando o valor inicial e o valor final no eixo x 
plt.xlim([0,250])

plt.show()

#########################################################################

# RODAR: python oscilacao_antartica.py

#########################################################################
