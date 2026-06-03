import streamlit as st
import pandas as pd
from utils import fetch_competitor_data

st.set_page_config(page_title="Tableau des résultats", layout="wide")
st.title("🔍 Extraction & Table des Données")
st.markdown("Saisissez un mot-clé pour extraire la liste des applications concurrentes en temps réel.")

# Composant de saisie utilisateur
search_term = st.text_input("Mot-clé de recherche :", placeholder="Ex: mental health, productivity...")

if search_term:
    # --- CORRECTION ICI : On nettoie le mot-clé ---
    cleaned_term = search_term.strip().lower()
    
    # Indicateur visuel de chargement pendant l'appel API
    with st.spinner(f"Extraction des données sur le Google Play Store pour '{cleaned_term}'..."):
        df = fetch_competitor_data(cleaned_term)
        
    if not df.empty:
        # Sauvegarde des données dans le Session State pour le partage inter-pages
        st.session_state['competitor_data'] = df
        st.session_state['current_keyword'] = cleaned_term
        
        st.success(f"Extraction réussie : {len(df)} applications trouvées.")
        
        # Affichage de la table de données interactive
        st.dataframe(df, use_container_width=True)
    else:
        st.error("Aucun résultat retourné par l'API. Essayez un autre terme.")
        