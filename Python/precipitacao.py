#Importando bibliotecas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd
import xarray as xr
import regionmask
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter,LatitudeFormatter

#Abrindo o arquivo shapefile
shapefile= gpd.read_file('baixo_iguacu.shp')
#print(shapefile.geometry)

#Transformar um objeto de poligono em array
poli = np.array(shapefile.geometry)     
#print(poli)

#Abrindo o arquivo Netcdf
df = xr.open_dataset('precip-total_GEFSav_glob_20221212T00.nc')
#print(df)

#Conversao dos dados de longitude do arquivo Netcdf
df.coords['lon']=((df.coords['lon'] + 180) % 360) - 180
df=df.sortby(df.lon)
#print(df)

#Editando as coordenadas de latitude e longitude do arquivo Netcdf 
ds = df.sel(lon=slice(-53.75,-51.75),lat=slice(-25.00,-26.75),time=slice('2022-12-12T06:00:00','2022-12-27T06:00:00'))
#print(ds)

# Criando uma mascara para a regiao do shapefile
poligono = regionmask.Regions(poli)
mask = poligono.mask(ds.isel(time=0),lat_name='lat',lon_name='lon')
prec_mask = ds.where(mask==0)
#print(prec_mask)

#Definindo precipitacao da regiao de mascara
prec = prec_mask['tp']
#print('PRECIPITAÇÃO' '\n',prec)

#Calculando a precipitacao media da regiao de mascara 
media_prec = prec.mean(dim='time')
#print('PRECIPITAÇÃO MÉDIA' '\n',media_prec)

#Criando um objeto de figura para receber o mapa e um eixo com uma determinada projeção
fig, ax = plt.subplots(subplot_kw={'projection':ccrs.PlateCarree()},figsize=(10,8))

#Definindo o tipo de barra lateral 
cbar_kwargs = {'label':'kg/m**2',
                'fraction':0.03,
                 'shrink':0.7}

#Plotando a variavel de interese e o shapefile
media_prec.plot(cbar_kwargs=cbar_kwargs)
shapefile.plot(ax=ax,facecolor='None',edgecolor='black')
     
#Fixando os valores de longitude na figura
ax.set_xticks([-53.5,-53.0,-52.5,-52.0,-51.5],crs=ccrs.PlateCarree())
plt.xlabel('Longitude')

#Fixando os valores de latitude na figura
ax.set_yticks([-26.5,-26.0,-25.5,-25.0],crs=ccrs.PlateCarree())
plt.ylabel('Latitude')

#Adicionando o titulo da figura 
plt.title('Precipitação média prevista(15 dias) Modelo GEFS\n(06UTC/12/12/2022 - 06UTC/27/12/2022)',
          fontdict={ 'family':'monospace',
                     'color':'black',
                     'weight':'bold',
                     'size':13})
plt.show()

##################################################################
#
#           RODAR O CÓDIGO: python3 precipitacao.py
#
##################################################################
