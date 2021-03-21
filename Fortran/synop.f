C###################################################################
C 202005022300 AAXX 02231 86973 26/// /1204 10165 20061 30110 40199

            INTEGER ANO(48),MES(48),DIA(48),HORA1(48),HORA2(48),
     *              DATE(48),ESTACAO(48),DIR(48),VEL(48),GRUPO1(48),
     *              TEMP1(48),TEMP2(48),GRUPO2(48),DEW1(48),
     *              DEW2(48),GRUPO3(48),P_EST1(48),P_EST2(48),
     *              GRUPO4(48),SLP1(48),SLP2(48)
        CHARACTER*5 INDICE(48)
        CHARACTER*4 NOME(48)
        CHARACTER*1 NEB(48)               

        OPEN(1,FILE='saida.txt',STATUS='OLD')
        OPEN(2,FILE='dados.txt',STATUS='OLD')

       DO 100 I=1,48

        READ(1,10)ANO(I),MES(I),DIA(I),HORA1(I),HORA2(I),NOME(I),
     *            DATE(I),ESTACAO(I),INDICE(I),NEB(I),DIR(I),VEL(I),
     *            GRUPO1(I),TEMP1(I),TEMP2(I),GRUPO2(I),DEW1(I),
     *            DEW2(I),GRUPO3(I),P_EST1(I),P_EST2(I),GRUPO4(I),
     *            SLP1(I),SLP2(I)               
10      FORMAT(I4,I2,I2,I2,I2,1X,A4,1X,I5,1X,I5,1X,A5,1X,A1,I2,I2,1X,
     *         I1,I3,I1,1X,I1,I3,I1,1X,I1,I3,I1,1X,I1,I3,I1,1X)

C       PRINT*, DIR(I),VEL(I) 



C PRESSÃO REDUZIDA AO NÍVEL MÉDIO DO MAR

       IF(SLP1(I).GE.0.AND.SLP1(I).LE.50)THEN
         SLP1(I) = SLP1(I) + 1000
       ELSE       
         IF(SLP1(I).GT.50)THEN
            SLP1(I) = SLP1(I)  
         ENDIF     
       ENDIF

C DIREÇÃO DO VENTO

       IF(DIR(I).GT.20)THEN
          DIR(I) = DIR(I)*10
       ELSE 
         IF(DIR(I).EQ.20)THEN 
            DIR(I) = DIR(I)*10
         ELSE 
            IF(DIR(I).LT.20.AND.DIR(I).GT.10)THEN  
              DIR(I)= DIR(I)*10     
            ELSE
              IF(DIR(I).EQ.10)THEN  
                 DIR(I) = DIR(I)*10  
              ELSE
                IF(DIR(I).LT.10)THEN
                   DIR(I) = DIR(I)*10   
                ENDIF  
              ENDIF
            ENDIF 
         ENDIF   
       ENDIF

C VELOCOIDADE DO VENTO

       VEL(I) = VEL(I)/0.51444

       PRINT*, DIR(I),VEL(I) 

       WRITE(2,20)ESTACAO(I),ANO(I),MES(I),DIA(I),HORA1(I),TEMP1(I),
     *            TEMP2(I),DEW1(I),DEW2(I),SLP1(I),SLP2(I),DIR(I),
     *            VEL(I) 
20     FORMAT(I5,1X,I4,1X,I2,1X,I2,1X,I2,1X,I2,'.',I1,1X,I2,'.',I1,
     *        1X,I4,'.',I1,1X,I3,1X,I2) 

100    CONTINUE

       END

C####################################################################
C           COMPILAR: gfortran synop.f
C              RODAR: ./a.out
C####################################################################
