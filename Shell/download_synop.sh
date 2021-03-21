#!/bin/bash

# CONTAR O NUMERO DE LINHAS DO ARQUIVO SYNOP.TXT
num=$(sed -n '$=' synop.txt)

#COMANDO PARA ACESSAR A TERCEIRA COLUNA DO ARQUIVO SYNOP.TXT
var=$(cut -d ' ' -f3 synop.txt)
#echo "$var"

echo '##############################################################'
echo '       O codigo vai extrair os dados SYNOP do site OGIMET     '
echo '##############################################################'

i=0
while [ $i -le $num ] ; do

 data_atual=$(date +%d/%m/%Y" "-" "%Hh%Mmin)

# COMANDO PARA CRIAR UM ARRAY E ARMAZENAR TODOS OS VALORES DE VAR
 vetor=(${var})
 estacao=$(echo "${vetor[$i]}")
  
# SINTAXE DO SITE
# https://www.ogimet.com/display_synops2.php?lugar=$estacao\&tipo=ALL\&ord=REV\&nil=SI\&fmt=txt\&ano=ANO_INICIAL\&mes=MES_INICIAL\&day=DIA_INICIAL\&hora=HORA_INICIAL\&anof=ANO_FINAL\&mesf=MES_FINAL\&dayf=DIA_FINAL\&horaf=HORA_FINAL\&enviar=Ver

 SITE=https://www.ogimet.com/display_synops2.php?lugar=$estacao\&tipo=ALL\&ord=REV\&nil=SI\&fmt=txt\&ano=2020\&mes=05\&day=01\&hora=00\&anof=2020\&mesf=05\&dayf=02\&horaf=23\&enviar=Ver

# CRIA UM ARQUIVO .TXT COM OS DADOS METEOROLÓGICOS DE CADA ESTAÇÃO
 lynx -dump $SITE > $estacao.txt

 echo "$i"
 i=$(($i + 1))

echo '      Estação: '$estacao
echo '         Data: '$data_atual
echo '--------------------------------------------------------------'

sleep 180

done

#####################################################################
#   COMPILAR: chmod a+x *.sh   
#      RODAR: ./pegar.sh
#####################################################################
