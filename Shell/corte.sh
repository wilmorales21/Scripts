#!/bin/bash

# comando para cortar os primeiras 15 caracteres de uma variavel do arquivo u.txt
var=$(cut -c 1-15 u.txt)
echo "$var"

#Escrevendo no arquivo de saída corte.txt
echo "$var"\n >> /home/user/corte.txt

#####################################################################
#   COMPILAR: chmod a+x *.sh   
#      RODAR: ./corte.sh
#####################################################################
