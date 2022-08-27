#!/bin/bash

# O comando awk vai colocar NaN no inicio de cada linha do arquivo vazio.csv
# e gerar um arquivo de saída chamado cheio.csv
awk '{print "NaN"$0}' vazio.csv > cheio.csv

################################################################
#          COMPILAR: chmod a+x *.sh
#             RODAR: ./put.sh
################################################################
