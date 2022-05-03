## Descrição
Foi escrito um código em shell para baixar os dados meteorológicos do tipo synop do site Ogimet, usando como base um cadastro das estações synop do Rio Grande do Sul(RS) com informações de latitude, longitude e número da estação. Obs:Para o código funcionar é preciso baixar o programa Linx!
O código corte.sh serve para editar as informações de vento zonal que estão no arquivo u.txt.

## Conteúdo do repositório
+ 86973.txt - Exemplo de arquivo que é baixado do site Ogimet com os dados meteorológicos das estações synop.
+ corte.sh - Código para cortar os 15 primeiros caracteres do arquivo com informações de vento zonal. 
+ corte.txt - Arquivo com as informações editadas de vento zonal. 
+ download_synop.sh - Código em shellscript para fazer o download dos dados synop das estações meteorológicas no site Ogimet.
+ synop.txt - Cadastro das estações meteorológicas synop do Rio Grande do Sul.
+ u.txt - Arquivo contendo informações de vento zonal.
