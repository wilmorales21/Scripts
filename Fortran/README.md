## Descrição(PT-BR)
O código synop.f serve para ajustar a pressão reduzida ao nível médio do mar, direção do vento e fazer a conversão da velocidade do vento a partir de dados meteorológicos das estações sinóticas. O código calculo_td.f serve para calcular a temperatura do ponto de orvalho a partir de informações de umidade específica e pressão. O código vento.f serve para calcular a direção do vento a partir de informações de vento zonal e vento meridional. O código pressao_reduzida.f serve para calcular a pressão reduzida ao nível médio do mar.
## Description(ENG)
The code synop.f serves to adapt the sea level pressure, wind direction and to do the conversion of the wind speed from meteorological datas of the synoptic stations. The code calculo_td.f serves to calculate the dew point temperature from datas of specific humidity and pressure. The code vento.f serves to calculate the wind direction from datas of zonal and meridional wind. The code pressao_reduzida.f serves to calculate pressure reduced to mean sea level.
## Descripción(ESP)
El codigo synop.f es para ajustar la pressión reducida al nivel medio del mar, dirección y hacer la conversión de la velocidad del viento a partir de datos meteorologicos de las estaciones sinópticas. El codigo calculo_td.f es para calcular la temperatura del punto de rocio a partir de datos del humedad específica y pressión. El codigo vento.f es para calcular la dirección del viento a partir de datos del viento zonal y viento meridional. El codigo pressao_reduzida.f es para calcular la pressión reducida al nivel medio del mar. 

## Conteúdo do repositório
+ calculo_td.f - Código para calcular a temperatura do ponto de orvalho a partir dos arquivos umidadeespecifica.txt e pressao.txt.
+ dados.txt - Arquivo com os dados meteorológicos organizados.
+ dados_estacoes.txt - Arquivo com dados meteorológicos com registro de pressão atmosférica sem a redução ao nível médio do mar.
+ direcao.txt - Arquivo com dados da direção do vento gerado pelo código vento.f.
+ estacoes.txt - Arquivo com dados de latitude, longitude e altitude de estações meteorológicas em algumas cidades do RS.
+ pressao.txt - Arquivo com dados de pressão atmosférica.
+ pressao_reduzida.f - Código para calcular a pressão reduzida ao nível médio do mar.
+ pressao_reduzida.txt - Arquivo com dados meteorológicos com a pressão reduzida ao nível médio do mar gerado pelo código pressao_reduzida.f.
+ saida.txt - Arquivo de dados meteorológicos synop observados.
+ synop.f - Código para organizar as variáveis meteorológicas, ajustar a pressão ao nível médio do mar e fazer conversão na velocidade do vento.
+ td.txt - Arquivo com dados de temperatura do ponto de orvalho gerado pelo código calculo_td.f.
+ u.txt - Arquivo com dados de velocidade zonal.
+ umidadeespecifica.txt - Arquivo com dados de umidade específica.
+ v.txt - Arquivo com dados de velocidade meridional.
+ vento.f - Código para calcular a direção do vento a partir dos arquivos u.txt e v.txt. 
