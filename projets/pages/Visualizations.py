import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Analyses Visuelles", layout="wide")
st.title("📈 Dashboard d'Analyse Concurrentielle")

# Sécurité : Vérification de la présence de données en mémoire
if 'competitor_data' not in st.session_state:
    st.warning("⚠️ Aucune donnée disponible. Veuillez d'abord soumettre un mot-clé sur la page '1_Results_Table'.")
else:
    df = st.session_state['competitor_data']
    keyword = st.session_state['current_keyword']
    
    st.info(f"Visualisations basées sur la recherche : **{keyword}**")

    # --- BARRE LATÉRALE (Filtre par Application ID) ---
    st.sidebar.header("Options de filtrage")
    app_options = ["Toutes les applications"] + list(df["Application ID"].unique())
    selected_app = st.sidebar.selectbox("Filtrer par ID d'application :", app_options)

    # Application dynamique du filtre de la barre latérale
    if selected_app != "Toutes les applications":
        df_plots = df[df["Application ID"] == selected_app]
    else:
        df_plots = df

    # --- DISPOSITION EN COLONNES (Layout) ---
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⭐ Distribution des Notes (Ratings)")
        fig_rating = px.histogram(
            df_plots, 
            x="Rating", 
            nbins=10, 
            title="Répartition des applications selon leur score",
            color_discrete_sequence=['#6366F1']
        )
        st.plotly_chart(fig_rating, use_container_width=True)

    with col2:
        st.subheader("💰 Modèle Économique")
        # Transformation des booléens en texte explicite
        modele_eco = df_plots["Free"].map({True: "Gratuit", False: "Payant"}).value_counts().reset_index()
        modele_eco.columns = ["Type", "Nombre"]
        
        fig_pie = px.pie(
            modele_eco, 
            names="Type", 
            values="Nombre", 
            title="Proportion d'applications gratuites vs payantes",
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    # --- TOP APPLICATIONS (Installations) ---
    st.markdown("---")
    st.subheader("🚀 Volume de Téléchargements")
    
    # Tri et extraction des 10 premières applications
    top_installed = df_plots.sort_values(by="Installs", ascending=False).head(10)
    
    fig_bar = px.bar(
        top_installed, 
        x="Installs", 
        y="Title", 
        orientation='h',
        title="Top 10 des applications les plus installées",
        text_auto='.2s',
        color="Rating",
        color_continuous_scale=px.colors.sequential.Plasma
    )
    fig_bar.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_bar, use_container_width=True)