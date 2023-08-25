# Movie_recommendation_system
Project for recommending movies based on TMDB dataset


# Movie Recommendation System using TMDB API

This is a movie recommendation system implemented in Python using the TMDB API. The system includes content-based filtering, collaborative filtering, and hybrid recommendation methods.

## Prerequisites

- Python 3.x
- Install required libraries by running:


## Getting Started

1. Obtain a TMDB API key:
 - Sign up on the [TMDB website](https://www.themoviedb.org/) to get an API key.
 - Replace `'YOUR_TMDB_API_KEY'` with your actual TMDB API key in the code.

2. Data Preparation:
 - Download the `ratings.csv` dataset containing user movie ratings.
 - Make sure your dataset is in the correct format with columns 'userId', 'movieId', and 'rating'.

3. Running the Recommendation System:
 - Open the `movie_recommendation.py` file.
 - Replace the TMDB API key and dataset filenames with appropriate values.
 - Run the script using:
   ```
   python movie_recommendation.py
   ```

## Usage

- Content-Based Filtering:
- Use the `content_recommendations` function to get movie recommendations based on movie content.
- Provide the movie title as input.

- Collaborative Filtering:
- Use the `collaborative_recommendations` function to get movie recommendations based on user ratings.
- Provide the movie ID as input.

- Hybrid Recommendation:
- Use the `hybrid_recommendations` function to get hybrid movie recommendations.
- Provide the movie title and user ID as inputs.

## Example Usage

```python
content_recs = content_recommendations('Inception')
collaborative_recs = collaborative_recommendations(296)
hybrid_recs = hybrid_recommendations('Inception', user_id=1)
