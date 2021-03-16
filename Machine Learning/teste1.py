########### importando bibliotecas ##########################
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

arq1 = open('alegrete.csv','r').read()
arq2 = open('variaveis.csv','w')

tex = str(arq1)

# Substituindo virgula por ponto
eb = tex.replace(',','.')

for x in eb:
 arq2.write(x)  

arq2.close()
#print('Feito?')

#-----------------------------------------------------------------------------------------
df = pd.read_csv('variaveis.csv',delimiter=' ',nrows=169)
#print(df)

# depois de testar com o codigo teste3.py para saber quais sao as variaveis mais importantes, temos:
# tmax,tmin,urins,urmin,tdins,tdmax

# definir a variavel alvo
y = df['tins']
print(y)

# definindo as variaveis tmax tmin urins urmin tdins tdmax para o dataframe x
a = df.drop(columns=['data'])
b = a.drop(columns=['utc'])
c = b.drop(columns=['tins'])
d = c.drop(columns=['urmax'])
e = d.drop(columns=['tdmin'])
f = e.drop(columns=['presins'])
g = f.drop(columns=['presmax'])
h = g.drop(columns=['presmin'])
i = h.drop(columns=['vel'])
j = i.drop(columns=['dir'])
l = j.drop(columns=['raj'])
m = l.drop(columns=['rad'])
x = m.drop(columns=['prec'])

print('dataframe x:')
print(x)

# a variavel alvo eh y e a variavel de teste eh x  

# importando bibliotecas de machine learning
from sklearn.model_selection import train_test_split

#criando conjunto de dados de treino e teste - o comando teste size indicarah que 80% dos dados serao pra teste e 20% pra treino
x_treino, x_teste, y_treino, y_teste = train_test_split(x,y, test_size=0.8,random_state=42)

#--------------------- Random Forest -------------------------------
# importando o algoritmo de machine learning Random Forest
from sklearn.ensemble import RandomForestRegressor

#criacao do modelo
#rfr = RandomForestRegressor(n_estimators=500,max_depth=1,random_state=30)
rfr = RandomForestRegressor()

#aplicar o algoritmo aos dados de treino usando a funcao fit
rfr.fit(x_treino,y_treino)

#imprimindo resultados
resultado = rfr.score(x_teste,y_teste)
print('Acuracia:', resultado*100)

#fazendo a previsao de y
y_previsto = rfr.predict(x_teste)
print('Y PREVISTO:\n',y_previsto)

from sklearn.metrics import mean_squared_error
from math import sqrt

#quanto menor for o valor da metrica rmse, melhor eh o modelo de previsao 
rmse = (np.sqrt(mean_squared_error(y_teste,y_previsto)))
print('RMSE: \n',rmse)

######################################################################
# suavizando a curva de machine leaning de temperatura

filter_length = 3
ml_suavizado = np.convolve(y_previsto,np.ones((filter_length)),mode='same')
ml_suavizado /= filter_length

######################################################################

# plota a temperatura observada
y.plot(color='olivedrab')

# plota a temperatura prevista pelo random forest
plt.plot(y_previsto,color='red')

#plota o machine learniong de temperatura suavizado
plt.plot(ml_suavizado,color='blue')

plt.title('Machine learning de temperatura')
plt.ylabel('Temperatura instantanea(°C)')

plt.grid()

plt.xticks([0,12,24,36,48,60,72,84,96,108,120,132,144,156],['01/01','12h','02/01','12h','03/01','12h','04/01','12h','05/01','12h','06/01','12h','07/01','12h'])
plt.xlim([0,167])

plt.show()

###################### Rodar o algoritmo no terminal ############################
#
#    RODAR O CODIGO: python teste7.py
#
#################################################################################
