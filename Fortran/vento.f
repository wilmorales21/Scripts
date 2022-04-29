C ESTE CÓDIGO FOI ESCRITO COM A AJUDA DA ALUNA DE PÓS-GRADUAÇÃO EM METEOROLOGIA DA USP, ANA MARIA.  
       PROGRAM DIRECAO_VENTO

C DECLARANDO AS VARIÁVEIS VENTO MERIDIONAL(V),VENTO ZONAL(U), X E ALFA
       REAL U(10), V(10), X(10), ALFA(10)

C FIXANDO O VALOR DE XPI     
       XPI = 180/3.1415927

C ABRINDO OS ARQUIVOS DE LEITURA E DE ESCRITA
       OPEN(1,FILE='u.txt',STATUS='OLD')
       OPEN(2,FILE='v.txt',STATUS='OLD')   
       OPEN(3,FILE='direcao.txt',STATUS='OLD') 

C LOOP DO CÓDIGO 
       DO 100 I=1,10

C LER OS ARQUIVO DE VENTO ZONAL
          READ(1,10)U(I)  
10        FORMAT(F20.17)
C          PRINT*, 'VENTO ZONAL', U(I)

C LER O ARQUIVO DE VENTO MERIDIONAL
          READ(2,20)V(I)  
20        FORMAT(F18.16)
C          PRINT*, 'VENTO MERIDIONAL', v(I)

C CALCULAR A MAGNITUDE DO VENTO 
C       VEL(I) = SQRT(U(I)**2 + V(I)**2)

C CALCULAR A DIREÇÃO DO VENTO
        X(I) = (ATAN(V(I)/U(I)))*XPI
        ALFA(I) = 90 - X(I)

        IF(U(I).GE.0)THEN
           ALFA(I) = ALFA(I) + 180
        ENDIF 
         
        PRINT*, 'ALFA = ', ALFA(I)
   
C ESCREVENDO A DIREÇÃO DO VENTO NO ARQUIVO DE SAÍDA CHAMADO direcao.txt        
       WRITE(3,30)ALFA(I)  
30     FORMAT(F10.6)

100    CONTINUE
      
       PRINT*, 'CERTO?' 
       END
  
C####################################################################
C           COMPILAR: gfortran vento.f
C              RODAR: ./a.out
C####################################################################
