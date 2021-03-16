import numpy as np
import pandas as pd


df = pd.read_csv('temperatura_diaria.csv', delimiter=' ',nrows=397)
ds = pd.read_csv('temperatura2020.csv',delimiter=' ',nrows=275)

x1 = df['datas']
x2 = ds['data5']

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
y22 = ds['ta20']

correlacao = ds['ta20'].corr(df['ta19'])
print('Correlacao(2020-2019) =', correlacao)
#print(correlacao)
#df.info()

# Correlacao 2020-2019 = 0.7460411775589699
# Correlacao 2020-2011 = 0.7687786016495036
# Correlacao 2020-2009 = 0.7512712642954986
# Correlacao 2020-2007 = 0.7640284005407132
# Correlacao 2020-2003 = 0.7454065021615686

#2020 - vermelho
#2019 - marrom
#2011 - azul
#2009 - verde
#2007 - roxo
#2003 - cinza
