#Importando bibliotecas
from pyspark.sql import SparkSession
from pyspark.sql.functions import max, min, avg
import pandas as pd
import math

# Criando uma sessão spark e configurando o nível de log para ERROR
spark = SparkSession.builder.appName("Exemplo").config("spark.driver.log.level", "ERROR").getOrCreate()

# Ler o arquivo Excel usando o Pandas
pandas_df = pd.read_excel('dados.xlsx')

# Criar um DataFrame do PySpark a partir do Pandas DataFrame
df = spark.createDataFrame(pandas_df)
#df.show()

# Agrupar por Preço Unitário e calcular a média e o máximo da Idade
df_agrupado = df.groupBy('ClientID').agg(avg('UnitPrice'), max('UnitPrice'))
df_agrupado.show()

######################################################
#
# RODAR: python3 agregacao_personalizada.py
#
######################################################
