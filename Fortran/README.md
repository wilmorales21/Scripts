## Descrição
O código synop.f serve para ajustar a pressão reduzida ao nível médio do mar, direção e a conversão da velocidade do vento a partir de dados meteorológicos das estações synop. O código fortran gera uma saída com os dados meteorológicos synop mais organizados.
O código calculo_td.f serve para calcular a temperatura do ponto de orvalho a partir de informações de umidade específica e pressão.
O código vento.f serve para calcular a direção do vento a partir de informações de vento zonal e meridional.


## Conteúdo do repositório
+ calculo_td.f - Código para calcular a temperatura do ponto de orvalho a partir dos arquivos umidadeespecifica.txt e pressao.txt.
+ dados.txt - Arquivo com os dados meteorológicos organizados.
+ direcao.txt - Arquivo com dados da direção do vento gerado pelo código vento.f.
+ pressao.txt - Arquivo com dados de pressão atmosférica.
+ saida.txt - Arquivo de dados meteorológicos synop observados.
+ synop.f - Código para organizar as variáveis meteorológicas, ajustar a pressão ao nível médio do mar e fazer conversão na velocidade do vento.
+ td.txt - Arquivo com dados de temperatura do ponto de orvalho gerado pelo código calculo_td.f.
+ u.txt - Arquivo com dados de velocidade zonal.
+ umidadeespecifica.txt - Arquivo com dados de umidade específica.
+ v.txt - Arquivo com dados de velocidade meridional.
+ vento.f - Código para calcular a direção do vento a partir dos arquivos u.txt e v.txt. 
