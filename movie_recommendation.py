import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from tmdbv3api import TMDb
from tmdbv3api import Movie

# Step 1: Fetch Movie Data from TMDB
tmdb = TMDb()
tmdb.api_key = 'YOUR_TMDB_API_KEY'

movie = Movie()
popular_movies = movie.popular()
movies_data = []

for i in range(len(popular_movies)):
    movie_info = movie.details(popular_movies[i].id)
    movies_data.append(movie_info)

# Step 2: Content-Based Filtering
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.DataFrame(movies_data)
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['overview'].fillna(''))

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def content_recommendations(title):
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]

# Step 3: Collaborative Filtering
ratings = pd.read_csv('ratings.csv')  # Load your movie ratings dataset

pivot_table = ratings.pivot_table(index='userId', columns='movieId', values='rating')
movie_means = pivot_table.mean(axis=0)
pivot_table_filled = pivot_table.apply(lambda row: row - movie_means, axis=1)

def collaborative_recommendations(movie_id):
    similar_scores = pivot_table_filled.corrwith(pivot_table_filled[movie_id])
    similar_movies = pd.DataFrame(similar_scores, columns=['correlation'])
    similar_movies.dropna(inplace=True)
    similar_movies = similar_movies.join(movie_means)
    similar_movies = similar_movies.sort_values(by='correlation', ascending=False)
    return similar_movies.head(10)

# Step 4: Hybrid Recommendation
def hybrid_recommendations(title, user_id):
    content_recs = content_recommendations(title)
    movie_id = df[df['title'] == title]['id'].values[0]
    collaborative_recs = collaborative_recommendations(movie_id)

    user_rated_movies = ratings[ratings['userId'] == user_id]['movieId'].values
    hybrid_recs = collaborative_recs[~collaborative_recs.index.isin(user_rated_movies)]

    return hybrid_recs

# Usage examples:
content_recs = content_recommendations('Inception')
collaborative_recs = collaborative_recommendations(296)
hybrid_recs = hybrid_recommendations('Inception', user_id=1)
