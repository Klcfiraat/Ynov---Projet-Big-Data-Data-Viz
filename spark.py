from pyspark.sql import SparkSession
import pandas as pd
import json
import requests
from pyspark.sql.types import StructType, StructField, FloatType, IntegerType,StringType

# Spark session & context
spark = (SparkSession
         .builder
         .master('local')
         .appName('meteo-consumer')
         # Add kafka package
         .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1")
         .getOrCreate())
sc = spark.sparkContext


df = (spark
  .readStream
  .format("kafka")
  .option("kafka.bootstrap.servers", "kafka:9092") # kafka server
  .option("subscribe", "projet") # topic
  .option("startingOffsets", "earliest") # start from beginning
  .load())


# Spark session & context
spark = (SparkSession
         .builder
         .master('local')
         .appName('meteo-consumer')
         # Add kafka package
         .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1")
         .getOrCreate())
sc = spark.sparkContext
df = (spark
  .readStream
  .format("kafka")
  .option("kafka.bootstrap.servers", "kafka:9092") # kafka server
  .option("subscribe", "projet") # topic
  .option("startingOffsets", "earliest") # start from beginning
  .load())


# recuperation des donnÃ©es directement depuis l'api 
url = "https://api.openweathermap.org/data/2.5/box/city?bbox=3.183905,48.124541,13.027655,50.585558,16&appid=6916f84569c84a0cc1ca9d6610eee79e"
df_nom = pd.DataFrame(columns=["id","dt","name","lat","lon","visibility","wind","rain","temp"])

for p, element in enumerate(requests.get(url).json()['list']):
    df_nom.loc[len(df_nom)-1] = [
        element['id'],
        element['dt'],
        element['name'],
        element['coord']['Lat'],
        element['coord']['Lon'],
        element['visibility'],
        element['wind']['speed'],
        element['rain'],
        element['main']['temp']
    ]

#definition du schema
df_schema = StructType([StructField("id", IntegerType(), True)\
                       ,StructField("dt", IntegerType(), True)
                       ,StructField("name", StringType(), True)
                       ,StructField("lat", FloatType(), True)
                       ,StructField("lon", FloatType(), True)
                       ,StructField("visibility", IntegerType(), True)
                       ,StructField("wind", FloatType(), True)
                       ,StructField("rain", IntegerType(), True)
                       ,StructField("temp", FloatType(), True)
                       ])
#conversion en spark dataframe
df = spark.createDataFrame(df_nom, schema=df_schema)
#affichage du dataframe
df.show()