# recommend.py
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load movie data
def load_data():
    movies = pd.read_csv("data/u.item", sep='|', encoding='latin-1', header=None,
                         names=["movie_id", "movie_title", "release_date", "video_release_date", "IMDb_URL",
                                "unknown", "Action", "Adventure", "Animation", "Children", "Comedy", "Crime",
                                "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery",
                                "Romance", "Sci-Fi", "Thriller", "War", "Western"])
    return movies

# Simple Content-Based Filtering using genre vectors
def build_recommender():
    movies = load_data()
    genre_features = movies.iloc[:, 5:]  # Genre columns
    similarity = cosine_similarity(genre_features)
    return movies, similarity

def recommend_movies(movie_title, top_n=5):
    movies, similarity = build_recommender()
    
    # Find movie index
    idx = movies[movies['movie_title'].str.lower() == movie_title.lower()].index
    if len(idx) == 0:
        return ["Movie not found in database."]
    
    idx = idx[0]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    recommended_titles = [movies.iloc[i[0]].movie_title for i in sim_scores]
    return recommended_titles
