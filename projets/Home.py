import streamlit as st

# Configuration de la mise en page globale
st.set_page_config(page_title="Veille Concurrentielle", layout="wide")

st.title("📊 Plateforme de Veille Concurrentielle")
st.subheader("Analyse décisionnelle des applications du Google Play Store")

st.markdown("""
---
### 🛠️ Présentation du Projet
Cette application web interactive a été conçue pour centraliser et visualiser les données de marché de nos concurrents directs sur le Google Play Store. 

Elle permet de transformer des données brutes extraites par API en indicateurs visuels exploitables pour l'aide à la décision.

### 🚀 Fonctionnalités Clés
* **Collecte Dynamique (`utils.py`)** : Interrogation en temps réel de la plateforme Google Play à partir de n'importe quel mot-clé utilisateur.
* **Exploration Structurée (`1_Results_Table`)** : Filtrage et lecture des données brutes récoltées (identifiants, développeurs, volumes).
* **Analyse Statistique (`2_Visualizations`)** : Visualisation de la distribution des notes, du modèle économique (gratuit vs payant) et des volumes d'installations.

### 📋 Mode d'emploi
1. Utilisez le menu latéral gauche pour naviguer vers la page **1_Results_Table**.
2. Saisissez votre mot-clé cible (ex: *mental health*, *note taking*).
3. Basculez sur la page **2_Visualizations** pour explorer les graphiques mis à jour automatiquement.
""")