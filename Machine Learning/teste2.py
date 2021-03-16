########### importando bibliotecas ##########################

import pandas as pd

df = pd.read_csv('variaveis.csv',delimiter=' ',nrows=169)
print('Pegou as variaveis?')

############### pre-processamento ##############################

# definir a variavel alvo
#y = df['tins']

#quando os metodos precisam de dados inteiros
v = df['tins']
y = v.astype(int)

print(y)

# definindo a variavel de teste(tirando coluna por coluna as variaveis indesejadas) 
a = df.drop(columns=['data'])
b = a.drop(columns=['tins'])
x = b.astype(int)

print(x)

#------------------- testando quais sao as melhores variaveis para o dataframe usando selectkbest ---------

#from sklearn.feature_selection import SelectKBest
#from sklearn.feature_selection import chi2

#funcao pra selecao de variaveis, k eh o numero de variaveis mais importantes
#best_var = SelectKBest(score_func = chi2, k=5)

#executa a funcao de pontuacao em (x,y) e obtem os recursos selecionados
#exe = best_var.fit(x,y)

#reduz x para os recursos selecionados
#features = exe.transform(x)
#print('Features: \n',features)


# ------------EXISTE OUTRO METODO DE ESCOLHER AS MELHORES VARIAVEIS DO DATAFRAME ----------------------

#------------ testando quais sao as melhores variaveis para o dataframe --------------------

# importando algoritmo de machine learning ExtraTreesClassifier
from sklearn.ensemble import ExtraTreesClassifier

#criando o modelo
etc = ExtraTreesClassifier()

#aplicando o algoritmo aos dados de treino usando a funcao fit
etc.fit(x,y)

#imprimindo resultados das variavaeis mais importantes do dataframe
print((etc.feature_importances_)*100)

# -------------------------------------------------------------------------------------------


###################### Rodar o algoritmo no terminal ############################
#
#    RODAR O CODIGO: python teste6.py
#
#################################################################################
