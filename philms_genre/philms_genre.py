from typing import List
from imdb import IMDb

imdb_api = IMDb()

def scrape_top_movies() -> List:
    g = []
    top = imdb_api.get_top250_movies()
    for topmovie in top:
        movie = imdb_api.get_movie(topmovie.movieID)
        g += movie['genres']
    return set(g)