########### importando bibliotecas ##########################

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor

#############################################################

df = pd.read_csv('variaveis.csv',delimiter=' ',nrows=1009)
#print(df)

# definir a variavel alvo
y = df['tins']
print(y)

#definindo as demais variaveis
# essas são as séries selecionadas
z1 = df['tmax']
z2 = df['tmin']
z3 = df['tdins']
z4 = df['tdmax']
z5 = df['tdmin']

# concatenar as series
x = pd.concat([z1,z2,z3,z4,z5],axis=1)
print('serie x:',x)

#criando conjunto de dados de treino e teste - o comando teste size indicarah que 30% dos dados serao pra teste e 70% pra treino
x_treino, x_teste, y_treino, y_teste = train_test_split(x,y, test_size=0.3)
#,random_state=42)

#criar o indice das variáveis de entrada
categorical_features_indices = np.where(x.dtypes != np.float64)[0]

#Criação da máquina preditiva 
modelo = CatBoostRegressor(iterations=50,depth=3,learning_rate=0.1,loss_function='RMSE')

#Treino da maquina preditiva pra aplicar o algoritmo aos dados de treino usando a funcao fit
modelo.fit(x_treino,y_treino,cat_features = categorical_features_indices,    # variaveis
          eval_set = (x_teste, y_teste), plot=True) # eval_set = dados de teste(validação) e plot é para plotar o treinamento

#Teste da maquina preditiva pra aplicar o algoritmo aos dados de teste usando a funcao fit
modelo.fit(x_teste,y_teste,
           cat_features = categorical_features_indices, #variaveis
           eval_set=(x_teste, y_teste), plot=True)  # eval_set = dados de teste(validação) e plot é para plotar o teste

#fazendo a previsão dos dados de treino
previsao1 = modelo.predict(x_treino)

#fazendo a previsão dos dados de teste
previsao2 = modelo.predict(x_teste)

#Criando variaveis para armazenar as previsoes
A = previsao1
B = previsao2

#Concatenar os valores das previsoes numa só matriz
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

# plota a temperatura prevista pelo catboost
plt.plot(pf[770:938],color='red')

#plotar legendas
plt.plot(y[770:938],label='Observado',color='olivedrab')
plt.plot(pf[770:938],label='Previsto',color='red')
plt.legend()

#plota o titulo da figura
plt.title('Machine learning de temperatura(Catboost)')
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
#    RODAR O CODIGO: python3 catboost.py
#
#################################################################################
