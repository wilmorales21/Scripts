import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#import seaborn as sns

# abrindo os arquivos com os dados
df = pd.read_csv('temperatura_diaria.csv', delimiter=' ',nrows=397)
ds = pd.read_csv('temperatura2020.csv',delimiter=' ',nrows=275)

# conversao de uma coluna object para string
df['datas'] = df['datas'].astype('|S')
#df['datas'] = df['datas'].astype('|S80')

x1 = df['datas']
#print(x1)
#print(type(x1))

x2 = ds['data5']

#determinando as colunas dos anos
y1 = df['ta99']
y2 = df['ta00']
y3 = df['ta01']
y4 = df['ta02']
y5 = df['ta03']
y6 = df['ta04']
y7 = df['ta05']
y8 = df['ta06']
y9 = df['ta07']
y10 = df['ta08']
y11 = df['ta09']
y12 = df['ta10']
y13 = df['ta11']
y14 = df['ta12']
y15 = df['ta13']
y16 = df['ta14']
y17 = df['ta15']
y18 = df['ta16']
y19 = df['ta17']
y20 = df['ta18']
y21 = df['ta19']

y22 = ds['ta20']


fig = plt.figure()
ax = fig.add_subplot(1,1,1,fc='white')
ax.tick_params(axis='x',colors='black')
ax.tick_params(axis='y',colors='black')
ax.spines['bottom'].set_color('grey')
ax.spines['top'].set_color('grey')
ax.spines['right'].set_color('grey')
ax.spines['left'].set_color('grey')
ax.set_title('Média móvel de 30 dias da temperatura média diária')
ax.set_ylabel('Temperatura média diária (°C)')
#ax.set_xlabel('Tempo')

#calculo da media movel de 30 dias para cada ano
y1.rolling(30).mean().plot(color='lightgrey')
y2.rolling(30).mean().plot(color='lightgrey')
y3.rolling(30).mean().plot(color='lightgrey')
y4.rolling(30).mean().plot(color='lightgrey')
y5.rolling(30).mean().plot(color='lightgrey')
y6.rolling(30).mean().plot(color='lightgrey')
y7.rolling(30).mean().plot(color='lightgrey')
y8.rolling(30).mean().plot(color='lightgrey')
#y9.rolling(30).mean().plot(color='magenta')
y10.rolling(30).mean().plot(color='lightgrey')
#y11.rolling(30).mean().plot(color='mediumorchid')
y12.rolling(30).mean().plot(color='lightgrey')
#y13.rolling(30).mean().plot(color='dodgerblue')
y14.rolling(30).mean().plot(color='lightgrey')
y15.rolling(30).mean().plot(color='lightgrey')
y16.rolling(30).mean().plot(color='lightgrey')
y17.rolling(30).mean().plot(color='lightgrey')
y18.rolling(30).mean().plot(color='lightgrey')
y19.rolling(30).mean().plot(color='lightgrey')
y20.rolling(30).mean().plot(color='lightgrey')
y21.rolling(30).mean().plot(color='lightgrey')
#y22.rolling(30).mean().plot(color='red')

#y5.rolling(30).mean().plot(color='dimgrey')
y9.rolling(30).mean().plot(color='mediumorchid')
y11.rolling(30).mean().plot(color='olivedrab')
y13.rolling(30).mean().plot(color='cornflowerblue')
#y21.rolling(30).mean().plot(color='chocolate')
y22.rolling(30).mean().plot(color='red')


plt.grid()

#Ajustando os valores no eixo x
plt.xticks([29,60,88,119,149,180,210,241,272,302,333,363],['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'])
#Ajustando o valor inicial e final no eixo x 
plt.xlim([29,393])

plt.show()

#####################################################
