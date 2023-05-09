import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import datetime

# Configuration de la page
st.set_page_config(
    page_title="Quête WildCodeSchool",
    layout="wide",
    page_icon="📐")
# titre
st.title('Hello Wilders, welcome to my application!')

#Sous_titre
st.write("I enjoy to discover streamlit possibilities")

#Sous_titre2
st.write("Voici le DF avec lequel je vais travailler.")

#Téléchargement du DF
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_car = pd.read_csv(link)

#Liste des noms des colonnes : continent, cubicinches, cylinders, hp, mpg, time-to-60, weightlbs, year
#Mise en format date de la colonne year
df_car["year"] = pd.to_datetime(df_car["year"]).dt.year
df_car['continent'] = df_car['continent'].str.replace('.', '')
pays = ["US", "Europe", "Japan"]

#Sidebar
def main():
	st.sidebar.header("Les filtres des pays ici :")
	pays_unique = df_car["continent"].unique()
	pays_choisi = st.sidebar.selectbox('Sélectionner un pays', pays_unique)
	df_select_pays = df_car[df_car['continent'] == pays_choisi]
	
	# afficher df
	st.dataframe(df_select_pays)
	
	# Afficher une analyse de corrélation
    	st.write('Map de corrélation')
	fig1, ax = plt.subplots()
	sns.heatmap(df_car.corr(), center=0,cmap = sns.color_palette("vlag", as_cmap=True))
	st.pyplot(fig1)	
		
	st.markdown("À partir de la carte thermique de corrélation, nous pouvons voir que la consommation des véhicules est fortement corrélée à leur puissance, leur masse et la taille de leur moteur. ")
	st.write("On constate une corrélation négative entre la consommation et l'année, ce qui signifie que les constructeurs ont tendance à faire des véhicules moins gourmands au fil des améliorations techniques.")
	st.write("Sans suprise, les véhicules plus lourds ont un moteur plus gros et une consommation supérieure aux plus légers.")

	
	# Ajouter un regplot de la relation entre puissance moteur et consommation
	st.write('Relation entre puissance moteur et consommation')
	fig2, ax = plt.subplots()
	sns.regplot(x="hp", y="time-to-60", data=df_select_pays, ax=ax)
	st.pyplot(fig2)
	
	
	
if __name__ == '__main__':
	main()
