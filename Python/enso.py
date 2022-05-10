# Importando bibliotecas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Abrindo os arquivos com os dados
df = pd.read_csv('enso.csv', delimiter=' ',nrows=253)

# Conversao de uma coluna object para string
df['MES'] = df['MES'].astype('|S')

x1 = df['MES']
#print(x1)

# Determinando a coluna de ENSO
y1 = df['ENSO']
#print(y1)

# Determinando as colunas dos anos
y2 = df['YEAR']
#print(y2)

# Plotando a curva da ENSO
y1.plot(color='grey')

# Este foi o último comando do código!!!
# Criar 252 valores no eixo x de 0 a 250
x1 = np.linspace(0,250,252)

# Preencher as areas positivas acima de 0.5 com a cor vermelha
plt.fill_between(x1,y1,0.5,where=y1>0.5,color='red',interpolate=True)

# Preencher as areas negativas abaixo de -0.5 com a cor azul
plt.fill_between(x1,y1,-0.5,where=y1<-0.5,color='blue',interpolate=True)

# Colocando um titulo na figura
plt.title('Evolução mensal do ENOS')

# Colocando um titulo no eixo x
plt.xlabel('Anos')

# Colocando um titulo no eixo y
plt.ylabel('Índice de ENOS')

# Comando para plotar uma linha horizontal no meio da figura
plt.axhline(0.5, color='black', lw= 0.5, linestyle= '-')
plt.axhline(0, color='black', lw= 0.5, linestyle= '-')
plt.axhline(-0.5, color='black', lw= 0.5, linestyle= '-')

# Ajustando o intervalo de valores no eixo y
plt.ylim([-3.0, 3.0])

# Determinando os valores no eixo y
plt.yticks([-3.0,-2.0,-1.0,0,1.0,2.0,3.0])

# Ajustando os valores no eixo x
plt.xticks([0,24,48,72,96,120,144,168,192,216,240],['2000','2002','2004','2006','2008','2010','2012','2014','2016','2018','2020'])

# Ajustando a posição do valor inicial e do valor final no eixo x 
plt.xlim([0,250])

plt.show()

#########################################################################

# RODAR: python enso.py

#########################################################################
