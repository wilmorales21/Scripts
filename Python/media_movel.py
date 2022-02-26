import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# abrindo os arquivos com os dados
df = pd.read_csv('temperatura_diaria.csv', delimiter=' ',nrows=397)

# conversao de uma coluna object para string
df['datas'] = df['datas'].astype('|S')
#df['datas'] = df['datas'].astype('|S80')

x1 = df['datas']
#print(x1)

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
y22 = df['ta20']


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

#calculo da media movel de 30 dias para cada ano
y1.rolling(30).mean().plot(color='lightgrey',label='1999')
y2.rolling(30).mean().plot(color='lightgrey',label='2000')
y3.rolling(30).mean().plot(color='lightgrey',label='2001')
y4.rolling(30).mean().plot(color='lightgrey',label='2002')
y5.rolling(30).mean().plot(color='lightgrey',label='2003')
y6.rolling(30).mean().plot(color='lightgrey',label='2004')
y7.rolling(30).mean().plot(color='lightgrey',label='2005')
y8.rolling(30).mean().plot(color='lightgrey',label='2006')
y10.rolling(30).mean().plot(color='lightgrey',label='2008')
y12.rolling(30).mean().plot(color='lightgrey',label='2010')
y14.rolling(30).mean().plot(color='lightgrey',label='2012')
y15.rolling(30).mean().plot(color='lightgrey',label='2013')
y16.rolling(30).mean().plot(color='lightgrey',label='2014')
y17.rolling(30).mean().plot(color='lightgrey',label='2015')
y18.rolling(30).mean().plot(color='lightgrey',label='2016')
y19.rolling(30).mean().plot(color='lightgrey',label='2017')
y20.rolling(30).mean().plot(color='lightgrey',label='2018')
y21.rolling(30).mean().plot(color='lightgrey',label='2019')

# a correlação foi calculada em outro código
# Correlacao 2020-2011 = 0.7687786016495036
# Correlacao 2020-2009 = 0.7512712642954986
# Correlacao 2020-2007 = 0.7640284005407132

#separando os anos com maior correlação com 2020
y9.rolling(30).mean().plot(color='mediumorchid',label='2007')
y11.rolling(30).mean().plot(color='olivedrab',label='2009')
y13.rolling(30).mean().plot(color='cornflowerblue',label='2011')
y22.rolling(30).mean().plot(color='red',label='2020')

#plotar legenda
plt.legend(ncol=3,loc='lower left')

#plotar grade
plt.grid()

#Ajustando os valores no eixo x
plt.xticks([29,60,88,119,149,180,210,241,272,302,333,363],['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'])
#Ajustando o valor inicial e final no eixo x 
plt.xlim([29,393])

plt.show()

#####################################################
#
# RODAR O CODIGO: python media_movel.py
#
######################################################
