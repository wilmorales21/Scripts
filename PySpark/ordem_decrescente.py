#Importando bibliotecas
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, mean, avg
import pandas as pd
import math

# Criando uma sessão spark e configurando o nível de log para ERROR
spark = SparkSession.builder.appName("Exemplo").config("spark.driver.log.level", "ERROR").getOrCreate()

# Ler o arquivo Excel usando o Pandas
pandas_df = pd.read_excel('dados.xlsx')

# Criar um DataFrame do PySpark a partir do Pandas DataFrame
df = spark.createDataFrame(pandas_df)
#df.show()

#Ordenando dados por ordem decrescente
df_ordenado = df.orderBy(df.UnitPrice.desc())
df_ordenado.show()

######################################################
#
# RODAR: python3 ordem_decrescente.py
#
######################################################

