from kafka import KafkaProducer
from json import dumps
from time import sleep
import json
import time
import requests

try:
    producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda x: dumps(x).encode('utf-8'))
    print("Connexion à Kafka réussie")
    TOKEN = '6916f84569c84a0cc1ca9d6610eee79e'
    zoom = 16
    EuropeW = '3.183905,48.124541,13.027655,50.585558'
    EuropeE = '17.984474,48.723510,25.455177,51.866246'
    AsieW = '72.989052,28.244139,78.614052,31.595136'
    AsieE = '115.193519,32.842490,119.390297,35.317188'
    AfriqueN = '-4.328613,33.852170,0.439453,35.389050'
    AfriqueC = '12.325603,6.321483,16.939861,9.974979'
    AfriqueS = '19.827204,-8.148851,24.990778,-4.414764'
    AmériqueN = '-76.955032,42.559503,-71.110306,45.558631'
    AmériqueC = '-92.598430,13.389995,-87.808391,17.665328'
    AmériqueS = '-51.072407,-21.156289,-47.468892,-17.717346'

    Continent=[EuropeW,EuropeE,AsieW,AsieE,AfriqueN,AfriqueC,AfriqueS,AmériqueN,AmériqueC,AmériqueS]

    while True:
        for pays in Continent:
            response=requests.get(f'https://api.openweathermap.org/data/2.5/box/city?bbox={pays},{zoom}&appid={TOKEN}')
            data=response.json()
            producer.send('projet', value=data)
            producer.flush()
            print(f"Données des continents en cours d'envoi au consumer....")
        time.sleep(600)

except:
    print("Erreur lors de la connexion avec Kafka")
