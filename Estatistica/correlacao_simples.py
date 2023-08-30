# Importando bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Lendo o arquivo de dados 
df = pd.read_csv('dados.csv', delimiter=' ',nrows=51)
#print(df)

#Definindo variáveis A e B
variavel_a = df['grupoa'] 
#print('VARIAVEL A \n', variavel_a)

variavel_b = df['grupob']
#print('VARIÁVEL B \n', variavel_b)

#------------------------------------------------------------------
#CALCULANDO REGRESSÃO LINEASR SIMPLES

correlacao = df['grupoa'].corr(df['grupob'])
print('CORRELAÇÃO ENTRE A e B = ', correlacao)

#Encontrar os coeficientes angular e linear da correlação
from sklearn.linear_model import LinearRegression

# Preparando os dados
X = np.array(df['grupoa']).reshape(-1, 1)
y = np.array(df['grupob'])

# Criando o modelo de regressão linear
modelo = LinearRegression()

# Ajustando o modelo aos dados
modelo.fit(X, y)

#Coeficientes angular e linear
coeficiente_angular = modelo.coef_[0]
coeficiente_linear = modelo.intercept_

print('COEFICIENTE ANGULAR(BETA1) = ', coeficiente_angular)
print('CEFICIENTE LINEAR(BETA0) = ', coeficiente_linear)

#--------------------------------------------------------------
#PLOTANDO UM GRÁFICO DE DISPERSÃO SIMPLES
 
#Ajustando o valor da correlação para plotar no gráfico
correlacao_ajustada = round(correlacao,3)
print('CORRELAÇÃO AJUSTADA =',correlacao_ajustada)

# Calculando os coeficientes da reta de regressão
coef = np.polyfit(variavel_a, variavel_b, 1)
inclinacao = coef[0]
interceptar = coef[1]

plt.figure(figsize=(8, 6))
plt.plot(variavel_a, inclinacao * variavel_a + interceptar, color='black', linewidth=0.7, label='Reta de Regressão')
plt.scatter(variavel_a, variavel_b, color='blue', alpha=0.7, label=correlacao_ajustada)

plt.title('Dispersão entre Variável A e Variável B')
plt.xlabel('Variável A')
plt.ylabel('Variável B')

#Ajustando as cores da borda e a posição da legenda
legend = plt.legend()
legend.set_title('Correlação de Pearson')
legend.set_bbox_to_anchor((1.5, 2.5))
frame = legend.get_frame()
frame.set_edgecolor('black')

# Ajustar a posição da legenda
legend.set_bbox_to_anchor((0.32, 1)) 
plt.show()

#########################################################
#
# RODAR: python3 correlacao_simples.py
#
#########################################################
