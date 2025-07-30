import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from reviews.service import ReviewService
from movies.service import MovieService


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()

    if reviews:
        review_df = pd.json_normalize(reviews)
        st.write("Lista de avaliações:")
        AgGrid(
            data=review_df,
            fit_columns_on_grid_load=True,
            height=len(review_df) * 30 + 50,
            key="reviews_grid",
        )
    else:
        st.warning("Nenhuma avaliação encontrada!")


def add_review():
    review_service = ReviewService()
    movies_service = MovieService()
    movies = movies_service.get_movies()
    movie_names = {
        movie['title']: movie['id'] for movie in movies
    }
    st.header("Adicionar Nova Avaliação")
    selected_movie_name = st.selectbox(
        label="Selecione o filme:",
        options=list(movie_names.keys()),
    )
    stars = st.slider(
        label="Nota do filme:",
        min_value=0,
        max_value=5,
        step=1
    )
    comment = st.text_area(
        label="Comentário:",
        placeholder="Escreva seu comentário aqui...",
        height=200
    )
    if st.button('Adicionar'):
        new_review = review_service.create_review(
            movie_id=movie_names[selected_movie_name],
            stars=stars,
            comment=comment
        )
        if new_review:
            st.success(f"Avaliação para o filme {selected_movie_name} adicionada com sucesso!")
            st.rerun()
        else:
            st.error("Erro ao adicionar a avaliação.")
