import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import xarray as xr

import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter,LatitudeFormatter

ds = xr.open_dataset('variaveis_meteorologicas.nc')
#print(ds)

#Extraindo uma área(América do Sul) para plotar os dados
ds_subset = ds.sel(longitude=slice(-90,-20),latitude=slice(10,-60))
print(ds_subset)

# Definindo variáveis
t = ds_subset['t'] 
u = ds_subset['u']
v = ds_subset['v']
wspd = (u**2 + v**2)**(0.5)

#print(u)
#print(v)
#print(wspd)

#Criando um objeto de figura para receber o mapa
fig = plt.figure(figsize=(10, 8))

#Criando um eixo com uma determinada projeção
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())

#Criando matrizes de longitude e latitude
lon, lat = np.meshgrid(u.longitude, u.latitude)

#Plotando as linhas de corrente e intensidade do vento
# time=2 indica o terceiro horario(12z) e level=0 indica o primeiro nivel de pressao(850hPa) de cima pra baixo
strm= ax.streamplot(lon, lat, u.isel(time=2,level=0).values, v.isel(time=2,level=0).values,
# arrowsize será o tamanho da setas e density é para proximidade das linhas de corrente 
                   arrowsize=0.5, density = 7,
                   color=wspd.isel(time=2,level=0).values, 
                   cmap='jet',transform=ccrs.PlateCarree())

#Adicionando barra lateral
cbar = plt.colorbar(strm.lines)
cbar.set_label(label='Velocidade do vento(m/s)', size=20, weight='normal')
cbar.ax.tick_params(labelsize=12)

#Adicionando o contorno do continente
ax.add_feature(cfeature.COASTLINE)

#Adicionando os limites dos paises
ax.add_feature(cfeature.BORDERS)

#Fixando os valores de longitude na figura
ax.set_xticks([-80,-70,-60,-50,-40,-30],crs=ccrs.PlateCarree())

#Fixando os valores de latitude na figura
ax.set_yticks([-60,-50,-40,-30,-20,-10,0,10],crs=ccrs.PlateCarree())

#Adicionando o titulo da figura 
ax.set_title('Linhas de corrente em 850hPa\n29-04-2022 12Z', fontsize=20)
plt.show()

#############################################################
#
#              Rodar: python3 vento_netcdf.py
#
#############################################################
