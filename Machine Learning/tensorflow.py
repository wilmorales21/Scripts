########### importando bibliotecas ##########################
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tensorflow as tf
#############################################################

df = pd.read_csv('variaveis.csv',delimiter=' ',nrows=1009)
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

X_val,y_val = X1[:672],y1[:672]
X_treino1,y_treino1 = X1[672:770],y1[672:770]
X_teste,y_teste = X1[770:],y1[770:]

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
modelo1.fit(X_treino, y_treino, validation_data=(X_val,y_val), epochs=100)

# Acionando a função fit aos dados de teste
modelo.fit(X_teste,y_teste,validation_data=(X_val,y_val), epochs=50)

# Fazendo a previsão com os dados de treino
previsao1 = modelo.predict(X_treino).flatten()
print('previsao1')

# Fazendo a previsão com os dados de teste
previsao2 = modelo.predict(X_teste).flatten()
print('previsao2')

# Criar um novo dataframe que receba informações da temperatura observada a partir do dia 02/02 até o dia 08/02
resultado = pd.DataFrame('Previsao':previsao2,'Observado':temp[770:938])
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
plt.xticks([770,794,818,842,866,890,914,937],['02/02','03/02','04/02','05/02','06/02','07/02','08/02','09/02'])
#fixando os pontos limites entre valor inicial e valor final no eixo x
plt.xlim([770,937])

plt.show()

###################### Rodar o algoritmo no terminal ############################
#
#    RODAR O CODIGO: python3 tensorflow.py
#
#################################################################################
