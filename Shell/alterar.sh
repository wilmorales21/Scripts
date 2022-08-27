#!/bin/bash

# Comando para substuituir o carctere de virgula(,) por ponto(.) no arquivo alegrete
# e gerar um novo arquivo chamado alegrete.csv

tr ',' '.' < alegrete > alegrete.csv

################################################################
#          COMPILAR: chmod a+x *.sh
#             RODAR: ./alterar.sh
################################################################

