import pandas as pd
import streamlit as st
import json
import requests
import matplotlib.pyplot as plt
import urllib.request as urllib2
from urllib.request import urlopen
import numpy as np


st.title('Visualisation Météo')

url = "https://api.openweathermap.org/data/2.5/box/city?bbox=3.183905,48.124541,13.027655,50.585558,16&appid=6916f84569c84a0cc1ca9d6610eee79e"
df_nom = pd.DataFrame(columns=["id","dt","name","lat","lon","visibility","wind","rain","snow","clouds", "temp","pression","humidite"])


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
        element['snow'],
        element['clouds'],
        element['main']['temp'],
        element['main']['pressure'],
        element['main']['humidity']

    ]

url1 = "https://api.openweathermap.org/data/2.5/box/city?bbox=72.989052,28.244139,78.614052,31.595136,16&appid=6916f84569c84a0cc1ca9d6610eee79e"
df_nom2 = pd.DataFrame(columns=["id","dt","name","lat","lon","visibility","wind","rain","snow","clouds", "temp","pression","humidite"])
for p, element in enumerate(requests.get(url1).json()['list']):
    df_nom2.loc[len(df_nom2)-1] = [
        element['id'],
        element['dt'],
        element['name'],
        element['coord']['Lat'],
        element['coord']['Lon'],
        element['visibility'],
        element['wind']['speed'],
        element['rain'],
        element['snow'],
        element['clouds'],
        element['main']['temp'],
        element['main']['pressure'],
        element['main']['humidity']
    ]

st.dataframe(df_nom)

moyenneEW = df_nom['temp'].mean()
st.metric(label="Température moyenne en Europe de l'ouest", value=moyenneEW)

st.header("Carte des villes d'Europe de l'ouest")
st.map(pd.DataFrame({'lat' : df_nom['lat'].values, 'lon' : df_nom['lon'].values}))

moyenneAsiew = df_nom2['temp'].mean()
st.metric(label="Température moyenne en Asie de l'ouest", value=moyenneAsiew)

st.header("Carte des villes d'Asie de l'ouest")
st.map(pd.DataFrame({'lat' : df_nom2['lat'].values, 'lon' : df_nom2['lon'].values}))


x2 = df_nom2['humidite']
y2 = df_nom2['temp']

plt.scatter(x2,y2)

plt.title("Température en fonction de l'humidité en Asie de l'ouest ")
plt.xlabel('humidité en %')
plt.ylabel('Temperature en °C')

st.pyplot(plt)

st.button("rerun")

