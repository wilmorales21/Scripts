# Importando bibliotecas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.offsetbox import AnchoredOffsetbox,TextArea, VPacker

# Abrindo os arquivos com os dados
df = pd.read_csv('Variaveis.csv', delimiter=' ',nrows=169)

# definindo as variaveis
data = df['data']
hora = df['utc']
tins = df['tins']
tmax = df['tmax']
tmin = df['tmin']
urin = df['urins']
urmax = df['urmax']
urmin = df['urmin']
tdins = df['tdins']
tdmax = df['tdmax']
tdmin = df['tdmin']
pressins = df['presins']
pressmax = df['presmax']
pressmin = df['presmin']
vel = df['vel']
dire = df['dir']
raj = df['raj']
rad = df['rad']
prec = df['prec']

plt.figure(figsize=(8,8))

# PLotando a primeira figura
ax1 = plt.subplot(2,1,1)
plt.subplots_adjust(wspace = 0.35, hspace = 0.35)
plt.title('Temperaturas máximas e mínimas (°C)')
y1 = TextArea('Tmax',textprops=dict(color='red',size=12,rotation='vertical'))
y2 = TextArea('Tmin',textprops=dict(color='royalblue',size=12,rotation='vertical'))
y3 = VPacker(pad=3,sep=5,align='center',mode='equal',children=[y1,y2])
anchor_y3 = AnchoredOffsetbox(loc=5,child=y3,pad=0,frameon=False,bbox_to_anchor=(-0.05,0.5),bbox_transform=ax1.transAxes, borderpad=0)
ax1.add_artist(anchor_y3)
plt.plot(tmax,color='red')
plt.plot(tmin,color='royalblue')
plt.xticks([0,24,48,72,96,120,144,167],['01/01','02/01','03/01','04/01','05/01','06/01','07/01','08/01'])
plt.xlim([0,167])
plt.grid()

#Plotando a segunda figura
ax2 = plt.subplot(2,1,2)
plt.subplots_adjust(wspace = 0.35, hspace = 0.35)
plt.title('Umidade relativa e Precipitação')
ax2.set_ylabel('(mm)')
#Criar um array do indice 0 até 168 para fixar os valores no eixo x
x = np.array(range(0,168)) 
plt.bar(x,prec,color='royalblue')
plt.grid()
# Compartilhando o mesmo eixo x
ax3 = ax2.twinx()
y5 = TextArea('URmax(%)',textprops=dict(color='olivedrab',size=12,rotation='vertical'))
y6 = TextArea('URmin(%)',textprops=dict(color='orange',size=12,rotation='vertical'))
y7 = VPacker(pad=3,sep=5,align='center',mode='equal',children=[y5,y6])
anchor_y7 = AnchoredOffsetbox(loc=5,child=y7,pad=0,frameon=False,bbox_to_anchor=(1.09, 0.5),bbox_transform=ax3.transAxes, borderpad=0)
ax3.add_artist(anchor_y7)
plt.plot(urmax,color='olivedrab')
plt.plot(urmin,color='orange')
plt.xticks([0,24,48,72,96,120,144,167],['01/01','02/01','03/01','04/01','05/01','06/01','07/01','08/01'])
plt.xlim([0,167])
plt.show()

#####################################################
#
# RODAR O CODIGO: python3 meteograma.py
#
######################################################

