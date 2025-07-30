import streamlit as st
from movies.repository import MoviesRepository


class MovieService:

    def __init__(self):
        self.movies_repository = MoviesRepository()

    def get_movies(self):
        if 'movies' in st.session_state:
            return st.session_state.movies
        movies = self.movies_repository.get_movies()
        st.session_state.movies = movies
        return movies

    def create_movie(self, title, release_date, genre, actors, resume):
        movie = dict(
            title=title,
            release_date=release_date,
            genre=genre,
            actors=actors,
            resume=resume
        )
        new_movie = self.movies_repository.create_movie(movie)
        st.session_state.movies.append(new_movie)
        return new_movie

    def update_movie(self, movie_id, title, release_date, genre, actors, resume):
        movie = dict(
            title=title,
            release_date=release_date,
            genre=genre,
            actors=actors,
            resume=resume
        )
        updated_movie = self.movies_repository.update_movie(movie_id, movie)
        for i, m in enumerate(st.session_state.movie):
            if m['id'] == movie_id:
                st.session_state.movie[i] = updated_movie
                break
        return updated_movie

    def delete_movie(self, movie_id):
        return self.movies_repository.delete_movie(movie_id)

    def get_movies_stats(self):
        return self.movies_repository.get_movies_stats()
