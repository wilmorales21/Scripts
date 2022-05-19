# Importando bibliotecas 
import pandas as pd
import matplotlib.pyplot as plt

# Leitura do arquivo de dados 
df = pd.read_csv('temperatura_diaria.csv', delimiter=' ',nrows=397)

# Declarando variaveis e associando com cada ano
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

# No gráfico de dispersão a variável que queremos analisar o comportamento(dependente)
# fica no eixo y e a variável que ajudar a explicar o comportamento fica no eixo x.

#Adicionando a linha reta dos pontos maximos que cruza os pontos dispersos
max1 = max(max(y11),max(y22))
# Plotar gráfico de espalhamento entre 2020 e 2009(correlacao 2020-2009 = 0.7224867565750908)
plt.scatter(y11, y22,s=15,label='Correlacao de Pearson = 0.72')
plt.legend(loc='lower right')
# Plotar a reta entre os pontos
plt.plot([0,max1],[0,max1],color='grey')
#Titulo da figura
plt.title('Dispersão simples de temperatura média diária')
# Plotar titulo no eixo x
plt.xlabel('Temperatura média diária 2009')
# Plotar titulo no eixo y
plt.ylabel('Temperatura média diária 2020')
plt.show()

#Adicionando a linha reta dos pontos maximos que cruza os pontos dispersos
max2 = max(max(y13),max(y22))
# Plotar gráfico de espalhamento entre 2020 e 2011(correlacao 2020-2011 = 0.7455266845176493)
plt.scatter(y13, y22,s=15,label='Correlacao de Pearson = 0.74')
plt.legend(loc='lower right')
# Plotar a reta entre os pontos
plt.plot([0,max2],[0,max2],color='grey')
#Titulo da figura
plt.title('Dispersão simples de temperatura média diária')
# Plotar titulo no eixo x
plt.xlabel('Temperatura média diária 2011')
# Plotar titulo no eixo y
plt.ylabel('Temperatura média diária 2020')
plt.show()

#Adicionando a linha reta dos pontos maximos que cruza os pontos dispersos
max3 = max(max(y21),max(y22))
# Plotar gráfico de espalhamento entre 2020 e 2019(correlacao 2020-2019 = 0.729112545318315)
plt.scatter(y21, y22,s=15,label='Correlacao de Pearson = 0.72')
plt.legend(loc='lower right')
# Plotar a reta entre os pontos
plt.plot([0,max3],[0,max3],color='grey')
#Titulo da figura
plt.title('Dispersão simples de temperatura média diária')
# Plotar titulo no eixo x
plt.xlabel('Temperatura média diária 2019')
# Plotar titulo no eixo y
plt.ylabel('Temperatura média diária 2020')
plt.show()

#########################################################
#
#       RODAR: python dispersao.py
#
#########################################################
