# Importando bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn.linear_model import LinearRegression
import scipy.stats as stats

#Lendo o arquivo de dados 
df = pd.read_csv('dados.csv', delimiter=' ',nrows=51)
#print(df)

#Definindo variáveis A e B
variavel_a = df['grupoa'] 
#print('VARIAVEL A \n', variavel_a)

variavel_b = df['grupob']
#print('VARIÁVEL B \n', variavel_b)

#----------------------------------------------------------------
#ANALISANDO OUTLIERS COM MÉTODO BOX PLOT PARA AS VARIÁVEIS A e B

# Calcular os quartis e o IQR para o grupo A
q1_a = df['grupoa'].quantile(0.25)
q3_a = df['grupoa'].quantile(0.75)
iqr_a = q3_a - q1_a

# Calcular os limites do bigode para o grupo A
limite_inferior_a = q1_a - 1.5 * iqr_a
limite_superior_a = q3_a + 1.5 * iqr_a

# Calcular os quartis e o IQR para o grupo B
q1_b = df['grupob'].quantile(0.25)
q3_b = df['grupob'].quantile(0.75)
iqr_b = q3_b - q1_b

# Calcular os limites do bigode para o grupo B
limite_inferior_b = q1_b - 1.5 * iqr_b
limite_superior_b = q3_b + 1.5 * iqr_b

#Criando o gráfico Boxplot
plt.figure(figsize=(8, 6))

# Criar e plotar o boxplot para as duas variáveis
boxplot_dados = [df['grupoa'], df['grupob']]
plt.boxplot(boxplot_dados, vert=True, labels=['Variável A', 'Variável B'], medianprops={'color': 'black'})

# Calcular e plotar os limites do bigode para cada grupo
plt.axhline(limite_inferior_a, color='red', linestyle='dashed', label='Limite Inferior de A')
plt.axhline(limite_superior_a, color='green', linestyle='dashed', label='Limite Superior de A')
plt.axhline(limite_inferior_b, color='blue', linestyle='dashed', label='Limite Inferior de B')
plt.axhline(limite_superior_b, color='orange', linestyle='dashed', label='Limite Superior de B')

#Plotar os pontos das variáveis em cima do boxplot
plt.scatter(np.random.normal(1, 0.04, size=len(df['grupoa'])),df['grupoa'], color='lightblue', alpha=0.7, label='Variável A', marker='o')
plt.scatter(np.random.normal(2, 0.04, size=len(df['grupob'])),df['grupob'], color='lightcoral', alpha=0.7, label='Variável B', marker='o')

#Título da figura e rótulo vertical
plt.title('Boxplot - Variáveis A e B')
plt.ylabel('Valores')

# Ajustar a legenda
legend = plt.legend()
frame = legend.get_frame()
frame.set_edgecolor('black')

#Ajustando a posição da legenda
legend.set_bbox_to_anchor((0.67, 0.35))

#Mostar gráfico
plt.show()

#########################################################
#
# RODAR: python3 boxplot.py
#
#########################################################
