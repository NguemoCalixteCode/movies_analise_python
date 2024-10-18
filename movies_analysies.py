# Analyse de films

# 1. Importation des bibliothèques
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurer les styles de visualisation
sns.set(style='whitegrid')

# 2. Chargement du fichier CSV
df = pd.read_csv('movies_dataset.csv')
print(df.head())

# 3. Exploration des données
print(df.info())
print(df.describe())

# 4. Analyse des données

# Films les mieux notés
top_rated_movies = df.nlargest(10, 'imdb_score')
print(top_rated_movies[['title', 'imdb_score']])

# Genres les plus populaires
genre_counts = df['genre'].value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=genre_counts.index, y=genre_counts.values, palette='viridis')
plt.xticks(rotation=45)
plt.title('Genres les plus populaires')
plt.xlabel('Genre')
plt.ylabel('Nombre de films')
plt.show()

# Tendances de production par année
production_trends = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(14, 7))
sns.lineplot(x=production_trends.index, y=production_trends.values, marker='o')
plt.title('Tendances de production par année')
plt.xlabel('Année de sortie')
plt.ylabel('Nombre de films')
plt.grid()
plt.show()

# 5. Interprétation des résultats
# Résumé des découvertes clés
