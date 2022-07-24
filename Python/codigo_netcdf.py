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

# Converter informações de longitude de 0 a 360 para -180 a 180
#ds.coords['grid_xt'] = ((ds.coords['grid_xt'] + 180) % 360) - 180
#ds = ds.sortby(ds.grid_xt)
#print(ds)

#Extraindo uma área para plotar os dados
ds_subset = ds.sel(longitude=slice(-90,-20),latitude=slice(10,-60))
print(ds_subset)

# Definindo variáveis
z = ds_subset['z']
t = ds_subset['t'] 
u = ds_subset['u']
v = ds_subset['v']
wspd = (u**2 + v**2)**(0.5)
tc = t - 273.15

print(tc)

#Criando um objeto de figura para receber o mapa
fig = plt.figure(figsize=(10, 8))
#Criando um eixo com uma determinada projeção
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())
#Criando matrizes de longitude e latitude
lon, lat = np.meshgrid(tc.longitude, tc.latitude)
#Plotando a temperatura do ar
# time=3 indica o quarto horario(18z) e level=0 indica o primeiro nivel de pressao(850hPa) de cima pra baixo
im= ax.contourf(lon, lat, tc.isel(time=3,level=0), 
#               levels=np.arange(-12,36,2), # Fixando os valores de temperatura entre -12 e 36 celsius em 1000hPa
#               levels=np.arange(-18,34,2), # Fixando os valores de temperatura entre -18 e 34 celsius em 925hPa
               levels=np.arange(-18,30,2), # Fixando os valores de temperatura entre -18 e 30 celsius em 850hPa
               cmap='jet',transform=ccrs.PlateCarree())
#Adicionando barra lateral
cbar = plt.colorbar(im,ax=ax,pad=0.06, fraction=0.023)
cbar.ax.tick_params(labelsize=12)
#Adicionando o contorno do continente
ax.add_feature(cfeature.COASTLINE)
#Adicionando os limites dos paises
ax.add_feature(cfeature.BORDERS)
#Fixando os valores de longitude na figura
ax.set_xticks([-80,-70,-60,-50,-40,-30],crs=ccrs.PlateCarree())
#Fixando os valores de latitude na figura
ax.set_yticks([-50,-40,-30,-20,-10,0,10],crs=ccrs.PlateCarree())
#Adicionando o titulo da figura 
ax.set_title('Temperatura do ar (°C) em 850hPa\n29-04-2022 18Z', fontsize=20)
plt.show()

#############################################################
#
#              Rodar: python3 codigo_netcdf.py
#
########3####################################################

