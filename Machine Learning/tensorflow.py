########### importando bibliotecas ##########################
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tensorflow as tf
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

#---------------------------------------------------------------------------------

df = pd.read_csv('Variaveis.csv',delimiter=' ',nrows=169)
#print(df)

#Definindo a variavel alvo
temp = df['tins']
#print(temp)

def df_to_X_y(df,window_size=5):
    df_as_np = df.to_numpy()
    X = []
    y = []
    for i in range(len(df_as_np)-window_size):
      row = [[a] for a in df_as_np[i:i+window_size]]
      X.append(row) 
      label = df_as_np[i+window_size] 
      y.append(label)
    return np.array(X), np.array(y)

WINDOW_SIZE = 5
X1,y1 = df_to_X_y(temp,WINDOW_SIZE)

X_val,y_val = X1[:17],y1[:17]
X_treino1,y_treino1 = X1[17:140],y1[17:140]
X_teste,y_teste = X1[140:],y[140:]

#Importando bibliotecas
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import layers

modelo = Sequential([layers.Input((5,1)),
                     layers.LSTM(64),
                     layers.Dense(8,activation='relu'),
                     layers.Dense(1)])

modelo1.compile(loss='mse',
                optimizer=Adam(learning_rate=0.01),
                metrics=['mean_absolute_error'])

# Acionando a funcao fit aos dados de treino
modelo1.fit(X_treino, y_treino1, validation_data=(X_val,y_val), epochs=100)

# Acionando a função fit aos dados de teste
modelo.fit(X_teste,y_teste,validation_data=(X_val,y_val), epochs=50)

# Fazendo a previsão com os dados de treino
previsao1 = modelo.predict(X_treino).flatten()
print('previsao1')

# Fazendo a previsão com os dados de teste
previsao2 = modelo.predict(X_teste).flatten()
print('previsao3')

#Criando variaveis para armazenar as previsoes
A = previsao1
B = previsao2

#Concatenar os valores das previsoes numa só matriz
previsao_final = np.concatenate((A,B),axis=0)
print('previsao_final')

# Criar um novo dataframe que receba informações da temperatura observada  a partir do 2º dia e da previsão final
resultado = pd.DataFrame('Previsao':previsao_final,'Observado':temp[22:])
print(resultado)

##############################################################################
# plota a temperatura observada
plt.plot(resultado['Observado'],color='olivedrab')

# plota a temperatura prevista pelo tensorflow
plt.plot(resultado['Previsao'],color='red')

#plotar legendas
plt.plot(resultado['Observado'],label='Observado',color='olivedrab')
plt.plot(resultado['Previsao'],label='Previsto',color='red')
plt.legend()

#plota o titulo da figura
plt.title('Machine learning de temperatura(Tensorflow)')
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
#    RODAR O CODIGO: python3 tensorflow.py
#
#################################################################################
