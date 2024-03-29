# Descrição(PT-BR)
Foi calculada a média móvel de 30 dias da temperatura média diária da cidade de Pelotas-RS, Brasil, entre os anos de 1999 e 2020 pelo código media_movel.py
a partir do arquivo de dados temperatura_diaria.csv. Foi calculada a correlação de Pearson entre o ano de 2020 e todos outros anos pelo código
correlacao.py. Em seguida, foi plotado o gráfico de dispersão simples entre os anos com correlação de Pearson acima de 0.70 pelo código dispersão.py a
partir do arquivo de dados temperatura_diaria.csv. Foi plotado o gráfico de barras de precipitação mensal dos anos com correlação de Pearson acima de 0.70 pelo código precipitacao.py. Também foi plotada a evolução mensal do índice de El Niño Oscilação Sul(ENOS) entre os anos de 2000 e 2021 pelo código enso.py a partir do arquivo de dados enso.csv. Foram plotadas a temperatura do ar no nível de pressão de 850hPa pelo código temperatura_netcdf.py e as linhas de corrente no nível de pressão de 850hPa pelo código vento_netcdf.py ambos a partir do arquivo variaveis_meteorologicas.nc que não estão neste repositório. Por último, foi plotado um meteograma com temperatura, umidade relativa e precipitação da estação automática do INMET em Alegrete pelo código meteograma.py a partir do arquivo Variaveis.csv. Foi plotada a precipitação média prevista pelo modelo GEFS sobre a Bacia do Baixo Iguaçu a partir de dados da geometria da bacia do arquivo baixo_iguacu.shp e do arquivo precip-total_GEFSav_glob_20221212T00.nc que não está neste repositório. 

# Description(ENG)
It was calculated the 30 days moving average for daily mean temperature in the city of Pelotas-RS, Southern of Brazil, between 1999 and 2020 by the
media_movel.py code from temperatura_diaria.csv data set. Then it was calculated the Pearson correlation between the year of 2020 and other years by the
correlacao.py code. It was ploted the simple scatter plot between the years with Pearson correlation above 0.70 by the dispersao.py code from temperatura_diaria.csv data file. It was ploted the bar graphic of monthly precipitation of the years with Pearson correlation above 0.70 by the precipitacao.py code. It was also ploted the monthly evolution of the El Niño Southern Oscillation(ENSO) index between 2000 and 2021 by the enso.py code from enso.csv data set. It were ploted the air temperature in the 850hPa pressure level by the codigo_netcdf.py code and the streamlines in the 850hPa pressure level by the vento_netcdf.py code both from variaveis_meteorologicas.nc file that are not in this repository. Lastly, it was ploted a meteogram with temperature, relative humidity and precipitation from INMET's automatic station in Alegrete by the meteograma.py code from Variaveis.csv file. It was ploted the mean precipitation forecasted by the GEFS model in the Baixo Iguaçu basin from basin geometry data of the baixo_iguacu.shp file and from precip-total_GEFSav_glob_20221212T00.nc file that is not in this repository.

# Descripción(ESP)
Fue calculada la média móvil de 30 dias de la temperatura média diária de la ciudad de Pelotas-RS, sur del Brasil, entre los años de 1999 y 2020 por el
código media_movel.py a partir del archivo de datos temperatura_diaria.csv. En seguida, fue calculada la correlación de Pearson entre el año de 2020 y
todos los otros años por el código correlacao.py. Fue plotado el gráfico de dispersión simples entre los años con correlación de Pearson arriba de 0.70 por el código dispersao.py a partir del archivo de datos temperatura_diaria.csv. Fue plotada el gráfico de barras de precipitación mensual de los años con correlación de Pearson arriba 0.70 por el código precipitacao.py. También fue plotada la evolución mensual del indice de El Niño Oscilación
Sur(ENOS) entre los años de 2000 y 2021 por el código enso.py a partir del archivo de datos enso.csv. Fueram plotadas la temperatura del aire en lo nível de pressión de 850hPa por el código codigo_netcdf.py y las líneas de corriente en lo nível de pressión de 850hPa por el código vento_netcdf.py ambos a partir do arquivo variaveis_meteorologica.nc que no están en esto repositório. Por ultimo, fue plotado un meteograma con temperatura, humedad relativa y precipitación de la estación automática del INMET in Alegrete por el código meteograma.py a partir del archivo Variaveis.csv. Fué plotada la precipitación média prevista por el modelo GEFS en la cuenca del Bajo Iguaçú a partir de los datos de la geometría de la cuenca del archivo baixo_iguacu.shp y del archivo precip-total_GEFSav_glob_20221212T00.nc que no está en esto repositório. 

<p align="center">   
   <img src="https://github.com/wilmorales21/Scripts/assets/80546143/128465ad-78ef-4cf9-822a-863ecc6a8e48" alt="media-movel" height="450">
</p>

Média móvel de 30 dias da temperatura média diária da cidade de Pelotas entre 1999 e 2020. Anos com correlação de Pearson acima de 0.70(colorido) e demais anos(cinza) - 30 days moving average of daily air temperature in the city of Pelotas-RS, southern of Brazil, between 1999 and 2020. Years with Pearson correlation above 0.70(colors) and other years(grey) - Média móvil de la temperatura del aire diaria en la ciudad de Pelotas-RS, sur del Brasil, entre los años de 1999 y 2020.Años con correlación de Pearson arriba de 0.70(colores) y otros años(gris).

<p align="center">   
   <img src="https://github.com/wilmorales21/Scripts/assets/80546143/fc5d823d-669b-411a-a4d6-5128bc598fe6" alt="precipitacao_temperatura" height="450">
</p>

Gráfico de barras de precipitação mensal dos anos com correlação de Pearson acima de 0.70 - Bar graphic of monthly precipitation of the years with Pearson correlation above 0.70 - Gráfico de barras de precipitación mensual de los años con correlación de Pearson arriba 0.70. 

<p align="center">   
   <img src="https://github.com/wilmorales21/Scripts/assets/80546143/5270ba1a-70c4-4753-81a9-5d6f8dce2929" alt="dispersao" height="400">
</p>

Gráfico de dispersão simples da temperatura média diária entre os anos de 2020 e 2011, onde a correlação de Pearson foi de 0.74 - Simple scatter plot of
daily average temperature between the years 2020 and 2011, where the Pearson correlation was 0.74 - Gráfico de dispersión simples de la temperatura média diária entre los años de 2020 y 2011, donde la correlación de Pearson fue de 0.74.

<p align="center">   
   <img src="https://github.com/wilmorales21/Scripts/assets/80546143/ad50689e-ba1f-4c42-b838-504bcd20d5ad" alt="enos" height="450">
</p>

Evolução mensal do índice de El Niño Oscilação Sul(ENOS).Anos com El Niño(vermelho), anos com La Niña(azul) e anos de neutralidade(branco) - Monthly evolution of the El Niño Southern Oscillation(ENSO) index. Years of El Niño(red), years of La Niña(blue) and years of neutrality(white)- Evolución mensual del índice de El Niño Oscilación Sur(ENOS).Años de El Niño(rojo), años de La Niña(azul) y años de neutralidad(blanco).

<p align="center">   
   <img src="https://github.com/wilmorales21/Scripts/assets/80546143/7b250520-523f-467a-b7e1-034b567f139a" alt="meteograma" height="500">
</p>

Meteograma de temperaturas máximas e mínimas em conjunto da umidade relativa máxima e mínima com precipitação da estação do INMET em Alegrete entre 01/01 e 07/01 de 2019 - Meteogram of maximum and minimum temperatures together maximum and minimum relative humidity with precipitation from the INMET station on Alegrete between 01/01 and 07/01 of 2019 - Meteograma de temperaturas máximas y mínimas en conjunto de la humidad relativa máxima y mínima con precipitación de la estación del INMET in Alegrete entre 01/01 y 07/01 de 2019. 

<p align="center">   
   <img src="https://github.com/wilmorales21/Scripts/assets/80546143/3f57907b-52a1-472d-96d7-d2ddd12166c3" alt="temperatura-850hpa" height="500">
</p>

Temperatura do ar no nível de pressão de 850hPa em 29/04/2022 - Air temperature in 850hPa level pressure on 29/04/2022 - Temperatura del aire en lo nível de pressión de 850hPa en 29/04/2022.

<p align="center">   
   <img src="https://github.com/wilmorales21/Scripts/assets/80546143/43fe4012-49a8-43dd-aa5d-46e9c24d48ee" alt="linhas-corrente-850hpa" height="500">
</p>

Linhas de corrente no nível de pressão de 850hPa em 29/04/2022 - Streamlines in 850hPa level pressure on 29/04/2022 - Líneas de corriente en lo nível de pressión de 850hPa en 29/04/2022. 

<p align="center">   
   <img src="https://github.com/wilmorales21/Scripts/assets/80546143/7a05df3d-25a1-4079-a63c-7685a8a85613" alt="chuva-prevista-bacia-iguacu" height="500">
</p>

Precipitação média para 15 dias prevista pelo modelo GEFS sobre a Bacia do Baixo Iguaçú.

## Conteúdo do repositório(PT-BR)
+ Variaveis.csv - Dados meteorológicos da estação automática do INMET em Alegrete-RS. 
+ correlacao.py - Código para calcular a correlação entre 2020 e os demais anos.
+ dispersao.py - Código para plotar o gráfico de dispersão simples entre os anos com correlação de Pearson acima de 0.70
+ dispersao2011-2020.png - Gráfico de dispersão simples entre os dados de temperatura média diária de 2011 e de 2020 com correlação de Pearson de 0.74.
+ enso.csv - Dados do índice mensal de El Niño Oscilação Sul(ENOS) entre os anos 2000 e 2021.
+ enos.png - Figura que mostra o índice mensal de El Niño Oscilação Sul(ENOS) entre 2000 e 2021.
+ enso.py - Código para plotar o índice mensal de El Niño Oscilação Sul(ENOS) entre 2000 e 2021.
+ linhas_de_corrente_850hpa.png -Figura que mostra as linhas de corrente no nível de pressão de 850hPa no dia 29/04/2022.
+ media_movel.py - Código para plotar a média móvel de 30 dias da temperatura do ar diária entre os anos de 1999 e 2020 para a cidade de Pelotas-RS, Brasil.
+ meteograma.png - Figura que mostra o meteograma de temperaturas máximas e mínimas, umidade relativa máximas e mínimas e precipitação.
+ meteograma.py - Código pra plotar o meteograma.
+ media_movel_temperatura.png - Figura que mostra a média móvel de 30 dias da temperatura do ar diária entre os anos de 1999 e 2020 para a cidade de Pelotas-RS, Brasil. Anos com correlação de Pearson acima de 0.70(colorido) e demais anos (cinza).
+ oscilacao_antartica.csv - Dados mensais do índice de Oscilação Antártica entre os anos 2000 e 2021.
+ oscilacao_antartica.py - Código para plotar o índice mensal de Oscilação Antártica entre os anos 2000 e 2021.
+ oscilação_antártica.png - Figura que mostra o índice mensal de Oscilação Antártica entre os anos 2000 e 2021.
+ precipitacao.csv - Dados de precipitação mensal de 2009,2011,2019 e 2020.
+ precipitacao.png - Figura que mostra o gráfico em barras da precipitação mensal.
+ precipitacao.py - Código para plotar o gráfico de barras da precipitação mensal dos anos com correlação de Pearson acima 0.70.
+ precipitacao_prevista - Código para plotar a previsão da precipitação média de 15 dias sobre a Bacia do Baixo Iguaçú pelo modelo GEFS
+ temperatura_850hPa.png - Figura que mostra a temperatura do ar no nível de pressão de 850hPa no dia 29/04/2022. 
+ temperatura_netcdf.py - Código para plotar a temperatura do ar a partir de dados NetCDF.
+ temperatura_diaria.csv - Dados de temperatura média diária observada entre 1999 e 2020 na cidade de Pelotas-RS, Brasil.
+ vento_netcdf.py - Código para plotar as linhas de corrente a partir dos dados Netcdf.

## Repository content(ENG)
+ Variaveis.csv - Meteorologicals data from INMET's automatic station in Alegrete-RS(southern of Brazil).
+ correlacao.py - This code calculate the Pearson correlation between the 2020 year e other years.
+ dispersao.py - This code serves to plot the simple scatter plot between the years with Pearson correlation above 0.70. 
+ dispersao2011-2020.png - Simple scatter plot between the daily average temperature datas of 2011 and 2020 with Pearson correlation above 0.74.
+ enso.csv - Data set of El Niño Southern Oscillation(ENSO) monthly index between 2000 and 2021. 
+ enos.png - This picture shows the El Niño Southern Oscillation(ENSO) monthly index between 2000 and 2021.
+ enso.py - This code plots the El Niño Southern Oscillation(ENSO) monthly index between 2000 and 2021.
+ linhas_de_corrente_850hpa.png - This picture shows the streamlines in 850hPa pressure level in 29/04/2022.
+ media_movel.py - This code calculate the 30 days moving average of air temperature daily between 1999 and 2020 for city of Pelotas-RS, southern of Brazil.
+ meteograma.png - This picture shows the meteogram of maximum and minimum temperatures, maximum and minimum relative humidity and precipitation.
+ meteograma.py - This code plots the meteogram.
+ média_movel_temperatura.png - This picture show the 30 days moving average of daily air temperature between 1999 and 2020 in the city of Pelotas-RS, southern of Brazil.Years with Pearson correlation above 0.70(colors) and other years(grey).
+ oscilacao_antartica.csv - Monthly data set of the Antartic Oscillation index between 2000 and 2021. 
+ oscilacao_antartica.py - This code plots the Antartic Oscillation monthly index between 2000 and 2021. 
+ oscilacao_antartica.png - This picture shows the Antartic Oscillation monthly index between 2000 and 2021
+ precipitacao.csv - Data set of monthly precipitation for the years 2009,2011,2019 and 2020.
+ precipitacao.png - This picture shows the bar graphic of the monthly precipitation. 
+ precipitacao.py - This code plots the bar graphic of the monthly precipitation for years with Pearson correlation above 0.70.
+ precipitacao_prevista.py - This code plot the the mean precipitation to 15 days predicted about the Baixo Iguaçú basin by the GEFS model
+ temperatura_850hPa.png - This picture shows the air temperature in 850hPa pressure level in 29/04/2022.
+ temperatura_netcdf.py - This code plots the air temperature from NetCDF data.
+ temperatura_diaria.csv - Data set of daily mean temperature observed between 1999 and 2020 in the city of Pelotas-RS, southern of Brazil
+ vento_netcdf.py - This code plots the streamlines in 850hPa pressure level in 29/04/2022.

## Contenido del repositorio(ESP)
+ Variaveis.csv - Datos meteorológicos de la estación del INMET in Alegrete-RS(sur del Brasil)
+ correlacao.py - Código para calcular la correlación de Pearson entre 2020 y los otros años.
+ dispersao.py - Código para plotar el gráfico de dispersión simples entre los años con correlación de Pearson arriba de 0.70.
+ dispersao2011-2020.png - Gráfico de dispersión simples entre los datos de temperatura média diária de 2011 y de 2020 con correlación de Pearson de 0.74.
+ enso.csv - Datos del índice mensual de El Niño Oscilación Sur(ENOS) entre los años de 2000 y 2021.
+ enos.png - Figura que ilustra el índice mensual de El Niño Oscilación Sur(ENOS) entre los años de 2000 y 2021.
+ enso.py - Código para plotar el índice mensual de El Niño Oscilación Sur(ENOS) entre los años de 2000 y 2021.
+ linhas_de_corrente_850hpa.png - Figura que muestra las líneas de corriente en lo nível de pressión de 850hPa en 29/04/2022.
+ media_movel.py - Código para plotar la média móvil de 30 dias de la temperatura del aire diaria entre los años de 1999 y 2020 para la ciudad de Pelotas-RS,sur del Brasil.
+ meteograma.png - Figura que ilustra el meteograma de temperaturas máximas y mínimas, humedad relativa máxima y mínima y precipitación.
+ meteograma.py - C
+ media_movel_temperatura.png - Figura que ilustra la média móvil de 30 dias de la temperatura del aire entre los años de 1999 y 2020 para la ciudad de Pelotas-RS, sur del Brasil. Años con correlación de Pearson arriba 0.70(colores) y otros años(gris).
+ oscilacao_antartica.csv - Datos mensuales del índice de Oscilación Antarctica entre los años de 2000 y 2021.
+ oscilacao_antartica.py - Código para plotar el índice mensual de Oscilación Antarctica entre los años de 2000 y 2021.
+ oscilacao_antartica.png - Figura que ilustra el índice mensual de Oscilación Antarctica entre los años de 2000 y 2021.
+ precipitacao.csv - Datos de precipitación mensual de 2009,2011,2019 e 2020.
+ precipitacao.png - Figura que muestra el gráfico en barras de la precipitación mensual.
+ precipitacao.py - Código para plotar el gráfico de barras de la precipitación mensual de los años con correlação de Pearson arriba 0.70.
+ precipitacao_prevista.py - Código para plotar la previsión de la precipitación média de 15 dias sobre la cuenca del Bajo Iguaçú por el modelo GEFS.
+ temperatura_850hPa.png - Figura que ilustra la temperatura del aire en lo nível de pressión de 850hPa en 29/04/2022.
+ temperatura_netcdf.py - Código para plotar la temperatura del aire a partir de datos NetCDF.
+ temperatura_diaria.csv - Datos de temperatura média diaria observada entre los años de 1999 y 2020 en la ciudad de Pelotas-RS,sur del Brasil.
+ vento_netcdf.py - Código plota las líneas de corrientes en 850hPa a partir de los datos Netcdf.
