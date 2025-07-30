import streamlit as st
from genres.repository import GenresRepository


class GenreService:

    def __init__(self):
        self.genres_repository = GenresRepository()

    def get_genres(self):
        if 'genres' in st.session_state:
            return st.session_state.genres

        genres = self.genres_repository.get_genres()
        st.session_state.genres = genres
        return genres

    def create_genre(self, name):
        genre = dict(
            name=name,
        )
        new_genre = self.genres_repository.create_genre(genre)
        st.session_state.genres.append(new_genre)
        return new_genre

    def update_genre(self, genre_id, name):
        genre = dict(
            name=name,
        )
        update_genre = self.genres_repository.update_genre(genre_id, genre)
        for i, g in enumerate(st.session_state.genres):
            if g['id'] == genre_id:
                st.session_state.genres[i] = update_genre
                break
        return update_genre

    def delete_genre(self, genre_id):
        sucess = self.genres_repository.delete_genre(genre_id)
        if sucess:
            st.session_state.genres = [genre for genre in st.session_state.genres if genre['id'] != genre_id]
        return sucess
