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
Ouvrir le notebook mongo et lancer les commandes. On peut voir qu'on récupère l'intégralité du message envoyé par le producer, et qu'on peut faire du requetage sur la base et obtenir les données météorologiques de Strasbourg par exemple.

### 8. Spark
Notre objectif avec Spark était de faire du traitement distribué avec par exemple une matrice de corrélation, des moyennes d'humidité, compter le nombre de villes où il neige, où il pleut...
Malheureusement, nous n'avons pas eu le temps de réparer nos problèmes de versions / dépendances avec les différents packages, même si le dataframe est bien construit.
Vous trouverez tout de même le code du notebook dans le répertoire.

### 9. Streamlit
Nous avons utilisé Streamlit pour faire de la visualisation sur une carte, des scatterplots... ce code est à lancer en invite de commande avec streamlit run streamlit.py
