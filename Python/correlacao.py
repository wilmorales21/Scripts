# Importando bibliotecas 
import numpy as np
import pandas as pd

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

# calculando a correlacao de Pearson
correlacao = y22.corr(y21)
print('Correlacao(2020-2019) =', correlacao)

correlacao = y22.corr(y20)
print('Correlacao(2020-2018) =', correlacao)

correlacao = y22.corr(y19)
print('Correlacao(2020-2017) =', correlacao)

correlacao = y22.corr(y18)
print('Correlacao(2020-2016) =', correlacao)

correlacao = y22.corr(y17)
print('Correlacao(2020-2015) =', correlacao)

correlacao = y22.corr(y16)
print('Correlacao(2020-2014) =', correlacao)

correlacao = y22.corr(y15)
print('Correlacao(2020-2013) =', correlacao)

correlacao = y22.corr(y14)
print('Correlacao(2020-2012) =', correlacao)

correlacao = y22.corr(y13)
print('Correlacao(2020-2011) =', correlacao)

correlacao = y22.corr(y12)
print('Correlacao(2020-2010) =', correlacao)

correlacao = y22.corr(y11)
print('Correlacao(2020-2009) =', correlacao)

correlacao = y22.corr(y10)
print('Correlacao(2020-2008) =', correlacao)

correlacao = y22.corr(y9)
print('Correlacao(2020-2007) =', correlacao)

correlacao = y22.corr(y8)
print('Correlacao(2020-2006) =', correlacao)

correlacao = y22.corr(y7)
print('Correlacao(2020-2005) =', correlacao)

correlacao = y22.corr(y6)
print('Correlacao(2020-2004) =', correlacao)

correlacao = y22.corr(y5)
print('Correlacao(2020-2003) =', correlacao)

correlacao = y22.corr(y4)
print('Correlacao(2020-2002) =', correlacao)

correlacao = y22.corr(y3)
print('Correlacao(2020-2001) =', correlacao)

correlacao = y22.corr(y2)
print('Correlacao(2020-2000) =', correlacao)

correlacao = y22.corr(y1)
print('Correlacao(2020-1999) =', correlacao)

#########################################################
#
#       RODAR: python correlacao.py
#
#########################################################
