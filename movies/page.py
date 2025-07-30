from datetime import datetime
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from movies.service import MovieService
from genres.service import GenreService
from actors.service import ActorService


def show_movies():
    movies_service = MovieService()
    movies = movies_service.get_movies()

    if movies:
        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['genre.id', 'actors'])
        st.write("Lista de Filmes:")
        AgGrid(
            data=movies_df,
            fit_columns_on_grid_load=True,
            height=len(movies_df) * 30 + 50,
            key="movies_grid",
        )
    else:
        st.warning("Nenhum filme encontrado!")


def add_movie():
    movies_service = MovieService()
    movies = movies_service.get_movies()

    st.header("Adicionar filme")
    title = st.text_input("Nome do filme:")
    release_date = st.date_input(
        label="Data de lançamento:",
        min_value="1800-01-01",
        max_value=datetime.today(),
        value=None,
        format="DD/MM/YYYY"
    )

    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {
        genre['name']: genre['id'] for genre in genres
    }
    selected_genre_name = st.selectbox(
        label="Gênero do filme:",
        options=list(genre_names.keys())
    )

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {
        actor['name']: actor['id'] for actor in actors
    }
    selected_actors_names = st.multiselect(
        label="Atores/Atrizes do filme:",
        options=list(actor_names.keys()),
        default=None,
    )
    selected_actors_ids = [actor_names[name] for name in selected_actors_names]
    resume = st.text_area("Resumo do filme:")

    if st.button('Adicionar'):
        existing_movies = [
            movie['title'].lower() for movie in movies
        ]
        if title.lower() in existing_movies:
            st.warning("Filme já existe!")
        elif title and genre_names and selected_actors_names:
            new_movie = movies_service.create_movie(
                title=title,
                release_date=release_date,
                genre=genre_names[selected_genre_name],
                actors=selected_actors_ids,
                resume=resume
            )
            if new_movie:
                st.success(f"Filme '{title}' adicionado com sucesso!")
                st.rerun()
            else:
                st.error("Erro ao adicionar o filme.")
        else:
            st.error("Por favor, insira os dados solicitados do filme.")
