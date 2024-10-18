import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le fichier CSV
df = pd.read_csv('movies_dataset.csv') 

# Afficher les premières lignes pour vérifier le chargement
print("Aperçu des données :")
print(df.head())

# Renommer les colonnes pour supprimer les espaces
df.columns = df.columns.str.strip()  # Enlève les espaces aux noms de colonnes

# Afficher les noms des colonnes après nettoyage
print("Noms de colonnes après nettoyage :")
print(df.columns)

# Convertir la colonne 'IMDb Rating' en type numérique
df['IMDb Rating'] = pd.to_numeric(df['IMDb Rating'], errors='coerce')

# Identifier les films avec le meilleur score IMDb
top_rated_movies = df.nlargest(10, 'IMDb Rating')
print("\nFilms les mieux notés :")
print(top_rated_movies[['Title', 'IMDb Rating']])

# Compter les occurrences de chaque genre
genre_counts = df['Genre'].value_counts()

# Visualiser les genres les plus populaires

plt.figure(figsize=(12, 6))
sns.barplot(x=genre_counts.index, y=genre_counts.values, palette='viridis')
plt.xticks(rotation=45)
plt.title('Genres les plus populaires')
plt.xlabel('Genre')
plt.ylabel('Nombre de films')
plt.show()

# Compter le nombre de films par année
production_trends = df['Year'].value_counts().sort_index()

# Visualiser les tendances de production
plt.figure(figsize=(14, 7))
sns.lineplot(x=production_trends.index, y=production_trends.values, marker='o')
plt.title('Tendances de production par année')
plt.xlabel('Année de sortie')
plt.ylabel('Nombre de films')
plt.grid()
plt.show()

