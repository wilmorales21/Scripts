#Importando bibliotecas
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import pandas as pd
import math

# Criando uma sessão spark e configurando o nível de log para ERROR
spark = SparkSession.builder.appName("Exemplo").config("spark.driver.log.level", "ERROR").getOrCreate()

# Ler o arquivo Excel usando o Pandas
pandas_df = pd.read_excel('dados.xlsx')

# Criar um DataFrame do PySpark a partir do Pandas DataFrame
df = spark.createDataFrame(pandas_df)
#df.show()

#Filtrar dados em condições complexas
df_filtrado_complexo = df.filter((col('UnitPrice') > 200.0) & (col('ClientID') != '14001'))
df_filtrado_complexo.show()

######################################################
#
# RODAR: python3 filtrar_dados_complexos.py
#
######################################################


