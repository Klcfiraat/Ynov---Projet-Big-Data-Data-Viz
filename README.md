# Ynov---Projet-Big-Data

## Projet d'architecture pour le cours de Big Data & Data Viz.

L'objectif est d'extraire des données d'une API pour les traiter et les stocker en utilisant un maximum de technologies vues en cours.
Vous trouverez ci-dessous les étapes pour reproduire l'architecture.

### 1. Récupérer le dossier docker-spark dans le répertoire

### 2. Déployer le container
Pour cela, il faut, dans le terminal, se rendre dans le dossier docker-spark et exécuter la commande docker-compose up, avec Docker lancé en fond.

### 3. Envoi du consumer dans le container Kafka
Exécuter la commande docker ps pour trouver l'id du container wurstmeister/kafka:2.11-2.0.0 (286569915f9d)
Se positionner dans le répertoire contenant le producer et le consumer puis exécuter la commande: docker cp consumer.py 286569915f9d:'root'

### 4. Accès et installation des librairies du container Kafka
Pour accéder dans le container : docker exec -it 286569915f9d bash.
Se rendre dans le répertoire root : cd root 

Python3 : apk add python3
Kafka : pip3 install kafka-python
Pymongo : pip3 install pymongo

### 5. Lancement du consumer et du producer
Lancer le consumer avec la commande python3 consumer.py
Accéder au producer.py en local et lancer la commande python3 producer.py

### 6. Etat des lieux
Ici, le consumer reçoit bien les données envoyées par le producer, qui correspondent aux données météorologiques des différentes régions.

### 7. MongoDB
