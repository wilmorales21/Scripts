# Importando bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import scipy.stats as stats

#Lendo o arquivo de dados 
df = pd.read_csv('dados.csv', delimiter=' ',nrows=51)
#print(df)

#Definindo variáveis A e B
variavel_a = df['grupoa'] 
#print('VARIAVEL A \n', variavel_a)

variavel_b = df['grupob']
#print('VARIÁVEL B \n', variavel_b)

#-------------------------------------------------------
#Calculando a média da variável A 
media_a = sum(variavel_a)/len(variavel_a)
#print('MÉDIA DA VARIÁVEL A \n', media_a)

#Calculando a média da variável B
media_b = sum(variavel_b)/len(variavel_b)
#print('MÉDIA DA VARIÁVEL B \n', media_b)

#Calculando a variância da variável A
variancia_a = sum((x - media_a)**2 for x in variavel_a) / len(variavel_a)
#print('VARIANCIA EM A \n', variancia_a)

#Calculando a variância da variável B
variancia_b = sum((y - media_b)**2 for y in variavel_b) / len(variavel_b)
#print('VARIANCIA EM B \n',variancia_b)

#Calculando o desvio-padrão na variável A
desvio_padrao_a = math.sqrt(variancia_a)
#print('DESVIO-PADRÃO EM A \n',desvio_padrao_a)

#Calculando o desvio-padrão na variável B
desvio_padrao_b = math.sqrt(variancia_b)
#print('DESVIO-PADRÃO EM B \n',desvio_padrao_b)

#---------------------------------------------------------
#TESTE DE HIPÓTESE T-STUDENT

tamanho_amostra = len(variavel_a)
#tamanho_amostra = len(variavel_b)
print('TAMANHO DA AMOSTRA =',tamanho_amostra)

# Cálculo do grau de liberdade
graus_liberdade = tamanho_amostra - 1
print('GRAU DE LIBERDADE =', graus_liberdade)

# Cálculo do valor crítico para um intervalo de confiança de 95%
valor_critico = stats.t.ppf(0.975, graus_liberdade)
print('VALOR CRITICO =', valor_critico)

#Cálculo da estatística t
estatistica_t = (media_a - media_b) / (desvio_padrao_a / tamanho_amostra + desvio_padrao_b / tamanho_amostra)**0.5
print('ESTATISTICA_T =',estatistica_t)

#Teste de hipótese
p_valor = 2 * (1 - stats.t.cdf(abs(estatistica_t), graus_liberdade))
print('P VALOR =',p_valor)

# Verificação da hipótese nula
if p_valor < 0.05:
    resultado = "Rejeitar a hipótese nula"
else:
    resultado = "Não rejeitar a hipótese nula"
print('RESULTADO =', resultado)

#------------------------------------------------------------------
#PLOTANDO O GRÁFICO DO TESTE T-STUDENT(FORMA DE SINO)

# Criação do gráfico
plt.figure(figsize=(8, 6))
# Valores de x para a curva
x = np.linspace(-4, 4, 1000)
# Densidade de probabilidade da distribuição t
y = stats.t.pdf(x, graus_liberdade, scale=1.5) 
plt.plot(x, y, label='Distribuição t')

# Preenchimento das áreas de rejeição
plt.fill_between(x, y, where=(x > valor_critico), color='red', alpha=0.3, label='Área de Rejeição')
plt.fill_between(x, y, where=(x < -valor_critico), color='red', alpha=0.3)

# Linhas verticais para valores críticos
plt.axvline(valor_critico, color='green', linestyle='dashed', label='Valor Critico Positivo')
plt.axvline(-valor_critico, color='green', linestyle='dashed', label='Valor Critico Negativo')

#Ajustando o valor crítico para plotar no eixo x
valor_critico_ajustado = round(valor_critico,3)
print('VALOR CRITICO AJUSTADO =',valor_critico_ajustado)

# Ajustar os valores no eixo x mantendo os outros valores
x_ticks_positions = np.arange(-4, 5)  # Posições dos valores no eixo x
x_ticks_labels = [-4, -3, str(-valor_critico_ajustado), -1, 0, 1, str(valor_critico_ajustado), 3, 4] 
plt.xticks(x_ticks_positions, x_ticks_labels)

# Formatação do gráfico
plt.xlabel('Estatística t')
plt.ylabel('Densidade de Probabilidade')
plt.title('Distribuição t com Teste T-Student')

#Ajustando as cores da borda e a posição da legenda
legend = plt.legend()
frame = legend.get_frame()
frame.set_edgecolor('black')

# Ajustar a posição da legenda
legend.set_bbox_to_anchor((0.5, 0.05)) 

# Exibição do gráfico
plt.show()

#########################################################
#
# RODAR: python3 teste_tstudent.py
#
#########################################################
