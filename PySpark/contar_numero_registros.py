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

#Contar o número total de registros no framework do spark
total_registros = df.count()
print("Total de registros:", total_registros)

######################################################
#
# RODAR: python3 contar_numero_registros.py
#
######################################################

