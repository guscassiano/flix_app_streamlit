import streamlit as st
import plotly.express as px

from movies.service import MovieService


def show_home():
    movie_service = MovieService()
    movies_stats = movie_service.get_movies_stats()

    st.header("Bem-vindo ao Flix App!")
    st.write("Use o menu lateral para navegar pelas diferentes seções do aplicativo.")
    st.write("Para começar, selecione uma opção no menu à esquerda.")
    st.write("")
    st.header("Estatísticas dos Filmes")

    if len(movies_stats['movies_by_genre']) > 0:
        fig = px.pie(
            movies_stats['movies_by_genre'],
            values='count',
            names='genre__name',
            title='Filmes por Gênero:',
        )
        st.plotly_chart(fig)

    st.write("Total de filmes: ", movies_stats['total_movies'])

    st.write("Total de avaliações: ", movies_stats['total_reviews'])

    st.write("Média de avaliações: ", movies_stats['average_stars'])

    st.write("")
    st.subheader("Quantidade de filme por gênero:")
    for genre in movies_stats['movies_by_genre']:
        st.write(f"{genre['genre__name']}: ", genre['count'])
