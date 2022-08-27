########### importando bibliotecas ##########################
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('variaveis.csv',delimiter=' ',nrows=1009)
#print(df)

# definir a variavel alvo
y = df['tins']
print(y)

# essas são as séries selecionadas
z1 = df['tmax']
z2 = df['tmin']
z3 = df['tdins']
z4 = df['tdmax']
z5 = df['tdmin']

# concatenar as series
x = pd.concat([z1,z2,z3,z4,z5],axis=1)
print('serie x:',x)

# a variavel alvo eh y e a variavel de teste eh x  

# importando bibliotecas de machine learning
from sklearn.model_selection import train_test_split

#criando conjunto de dados de treino e teste - o comando teste size indicarah que 30% dos dados serao pra teste e 70% pra treino
x_treino, x_teste, y_treino, y_teste = train_test_split(x,y, test_size=0.3)
#,random_state=42)

#--------------------- Random Forest -------------------------------
# importando o algoritmo de machine learning Random Forest
from sklearn.ensemble import RandomForestRegressor

#criacao do modelo
rfr = RandomForestRegressor()

#aplicar o algoritmo aos dados de treino usando a funcao fit
rfr.fit(x_treino,y_treino)
previsao1 = rfr.predict(x_treino)
print(previsao1)

#aplicar o algoritmo aos dados de teste usando a funcao fit
rfr.fit(x_teste,y_teste)
previsao2 = rfr.predict(x_teste)
print(previsao2)

#Criando variaveis para armazenar as previsoes
A = previsao1
B = previsao2

#Concatenar os valores das previsoes numa só variavel
previsao_final = np.concatenate((A,B),axis=0)
print('Previsao final:')
print(previsao_final)

# Converter dados de array para series 
pf = pd.Series(previsao_final)
print('Previsao final serie')
print(pf)

##############################################################################
# plota a temperatura observada
plt.plot(y[770:938],color='olivedrab')

# plota a temperatura prevista pelo random forest
plt.plot(pf[770:938],color='red')

#plotar legendas
plt.plot(y[770:938],label='Observado',color='olivedrab')
plt.plot(pf[770:938],label='Previsto',color='red')
plt.legend()

#plota o titulo da figura
plt.title('Machine learning de temperatura(Random Forest)')
plt.ylabel('Temperatura instantanea(°C)')
plt.xlabel('Dias')

#plota o grafico com grade
plt.grid()

#fixando valores no eixo x
plt.xticks([770,794,818,842,866,890,914,937],['02/02','03/02','04/02','05/02','06/02','07/02','08/02','09/02'])

#fixando os pontos limites entre valor inicial e valor final no eixo x
plt.xlim([770,937])

plt.show()

###################### Rodar o algoritmo no terminal ############################
#
#    RODAR O CODIGO: python3 randomforest.py
#
#################################################################################
