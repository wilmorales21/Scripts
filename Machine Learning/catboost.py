########### importando bibliotecas ##########################

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor

#############################################################

arq1 = open('Alegrete.csv','r').read()
arq2 = open('Variaveis.csv','w')


#converter todo o arq1 em string
tex = str(arq1)

# Substituindo virgula por ponto
eb = tex.replace(',','.')

for x in eb:
 arq2.write(x)  

arq2.close()
#print('Feito?')

#-----------------------------------------------------------------------------------------

df = pd.read_csv('Variaveis.csv',delimiter=' ',nrows=169)
#print(df)

# definir a variavel alvo
y = df['tins']
print(y)

#definindo as demais variaveis
x = df.drop(columns=['tins'])
print(x)

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

##############################################################################
# plota a temperatura observada
plt.plot(y,color='olivedrab')

# plota a temperatura prevista pelo catboost
plt.plot(previsao_final,color='red')

#plotar legendas
plt.plot(y,label='Observado',color='olivedrab')
plt.plot(previsao_final,label='Previsto',color='red')
plt.legend()

#plota o titulo da figura
plt.title('Machine learning de temperatura(Catboost)')
plt.ylabel('Temperatura instantanea(°C)')
plt.xlabel('Dias')

#plota o grafico com grade
plt.grid()

#fixando valores no eixo x
plt.xticks([24,48,72,96,120,144],['02/01','03/01','04/01','05/01','06/01','07/01'])
#fixando os pontos limites entre valor inicial e valor final no eixo x
plt.xlim([24,167])

plt.show()

###################### Rodar o algoritmo no terminal ############################
#
#    RODAR O CODIGO: python3 catboost.py
#
#################################################################################
