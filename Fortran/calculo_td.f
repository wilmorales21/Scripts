
       PROGRAM LER DADOS

C      DECLARANDO AS VARIÁVEIS UMIDADE ESPECÍFICA, PRESSÃO, EST E ORVALHO
       REAL UE(10), PRESS(10), EST(10), TD(10)

C ABRINDO OS ARQUIVOS DE LEITURA E DE ESCRITA
       OPEN(1,FILE='umidadeespecifica.txt',STATUS='OLD')
       OPEN(2,FILE='pressao.txt',STATUS='OLD')   
       OPEN(3,FILE='td.txt',STATUS='OLD')  

C LOOP DO CÓDIGO 
       DO 100 I=1,10

C LER OS ARQUIVO DE UMIDADE ESPECIFICA
          READ(1,10)UE(I)  
10        FORMAT(F18.15)
C          PRINT*, 'UMIDADE ESPECIFICA', UE(I)

C LER O ARQUIVO DE PRESSÃO
          READ(2,20)PRESS(I)  
20        FORMAT(F18.14)
C          PRINT*, 'PRESSÃO', PRESS(I)

C CALCULAR TEMPERATURA DO PONTO DE ORVALHO
           EST(I) = UE(I)*PRESS(I)/((622+UE(I))*6.11)
           TD(I) = (237.3*ALOG10(EST(I)))/(7.5-ALOG10(EST(I)))
           PRINT*, 'ORVALHO=',TD(I)
           
C ESCREVENDO TEMPERATURA DO PONTO DE ORVALHO NO ARQUIVO DE SAÍDA CHAMADO td.txt        
       WRITE(3,30)TD(I)  
30     FORMAT(F10.7)

100    CONTINUE

       PRINT*, 'CERTO?' 
       END
  
C####################################################################
C           COMPILAR: gfortran calculo_td.f
C              RODAR: ./a.out
C####################################################################
