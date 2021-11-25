from kafka import KafkaConsumer
from pymongo import *
import json
import pymongo

topic_name = "projet"

consumer = KafkaConsumer(
    topic_name,
     bootstrap_servers=['kafka:9093'],
     auto_offset_reset='latest',
     enable_auto_commit=True,
     auto_commit_interval_ms =  5000,
     fetch_max_bytes = 128,
     max_poll_records = 100,
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

try:
    client = MongoClient('mongo', 27017, username='root', password='example')
    db_meteo = client.meteo
    postmeteo = db_meteo.posts
    postmeteo.drop()
    print("Création de la base de données")

except:
    print("Erreur lors de la connexion avec MongoDB")

for message in consumer:
    message.offset
    msg = json.loads(json.dumps(message.value))
    print(msg)
    list = msg['list']
    for a in list:
        id=a['id']
        dt=a['dt']
        name=a['name']
        coord=a['coord']
        main=a['main']
        visibility=a['visibility']
        wind=a['wind']
        rain=a['rain']
        snow=a['snow']
        clouds=a['clouds']
        dict={"id":id,"dt":dt,"name":name,"coord":coord,"main":main,"visibility":visibility,"wind":wind,"rain":rain,"snow":snow,"clouds":clouds}
        postmeteo.insert_one(dict).inserted_id
