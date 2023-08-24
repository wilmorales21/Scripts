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

#Adicionar nova coluna e duplicar
df_transformado = df.withColumn('New_Quantity', col('Quantity') *2)
df_transformado.show()

######################################################
#
# RODAR: python3 adicionar_coluna.py
#
######################################################

