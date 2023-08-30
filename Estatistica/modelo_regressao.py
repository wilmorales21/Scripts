# Importando bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


#Lendo o arquivo de dados 
df = pd.read_csv('dados.csv', delimiter=' ',nrows=51)
#print(df)

#Definindo variáveis A e B
variavel_a = df['grupoa'] 
#print('VARIAVEL A \n', variavel_a)

variavel_b = df['grupob']
#print('VARIÁVEL B \n', variavel_b)

#--------------------------------------------------------------
#CRIANDO UM MODELO ESTATÍSTICO DE REGRESSÃO

#Definindo a variável de entrada
X = variavel_a
# Adicionar uma constante (intercepto) ao modelo
X = sm.add_constant(X)

#Definindo a variável de saída
y = variavel_b

#Criar um modelo de regressão
modelo = sm.OLS(y, X).fit()

#Resumo do modelo
print('RESUMO DO MODELO=',modelo.summary())

# Obter os resíduos do modelo
residuos = modelo.resid

#Criando uma coluna com os dados ajustados(previsão) por regressão linear para estimar a variavel dependente de saída y(grupob) 
df['valores_ajustados'] = modelo.predict(X)
previsoes = df['valores_ajustados']

# Criando os gráficos
plt.figure(figsize=(8, 6))
plt.scatter(previsoes, residuos, color='blue')
plt.axhline(0, color='red', linestyle='dashed')
plt.xlabel('Previsão')
plt.ylabel('Resíduos')
plt.title('Dispersão de Resíduos X Previsão')

plt.figure(figsize=(8,6))
sns.histplot(residuos, kde=True)
plt.xlabel('Resíduos')
plt.ylabel('Frequência')
plt.title('Histograma de Resíduos')

plt.figure(figsize=(8,6))
plt.scatter(residuos.index, residuos)
plt.axhline(0, color='red', linestyle='dashed')
plt.xlabel('Observações')
plt.ylabel('Resíduos')
plt.title('Resíduos X Observações')

plt.show()

#Criando um novo dataframe para concatenar as variaveis 'grupoa', 'grupob' e 'valores_ajustados'
df_combinado = pd.concat([df['grupoa'],df['grupob'],df['valores_ajustados']], axis=1)
print(df_combinado)

#Criar uma planilha em Excel
regressao_excel = 'regressao_estatistica.xlsx'
df_combinado.to_excel(regressao_excel, index=False)

#########################################################
#
# RODAR: python3 modelo_regressao.py
#
#########################################################
