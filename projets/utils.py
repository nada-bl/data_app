import pandas as pd
from google_play_scraper import search, app

def fetch_competitor_data(search_term):
    """
    Prend un mot-clé en paramètre, effectue une recherche via l'API Google Play
    et retourne un DataFrame Pandas contenant les détails des applications.
    """
    try:
        # Recherche des applications associées au mot-clé
        search_results = search(
            search_term,
            lang="en",
            country="us",
            n_results=30
        )
        
        # Si la recherche globale ne renvoie rien, on s'arrête tout de suite
        if not search_results:
            print("Aucun résultat global trouvé pour ce mot-clé.")
            return pd.DataFrame()
        
        detailed_apps = []
        
        # Récupération des détails pour chaque application trouvée
        for result in search_results:
            app_id = result.get('appId')
            if not app_id:
                continue
            try:
                info = app(app_id, lang="en", country="us")
                
                # Sécurisation des données avec .get() et des valeurs de secours
                detailed_apps.append({
                    "Application ID": info.get("appId", app_id),
                    "Title": info.get("title", "Inconnu"),
                    "Rating": info.get("score", 0.0 if info.get("score") is None else info.get("score")),
                    "Installs": info.get("realInstalls", 0),
                    "Price": info.get("price", 0.0),
                    "Free": info.get("free", True),
                    "Description": info.get("description", ""),
                    "Genre": info.get("genre", "Inconnu")
                })
            except Exception as e:
                # Si une application spécifique bloque, on l'ignore et on passe à la suivante
                print(f"Erreur pour l'application {app_id}: {e}")
                continue
                
        # Création du DataFrame final
        df = pd.DataFrame(detailed_apps)
        return df

    except Exception as e:
        print(f"Erreur générale lors de l'extraction API : {e}")
        return pd.DataFrame()