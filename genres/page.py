from time import sleep
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from genres.service import GenreService


def show_genres():
    genres_service = GenreService()
    genres = genres_service.get_genres()
    if genres is None:
        st.warning("Nenhum gênero encontrado.")

    else:
        st.write("Lista de Gêneros: ")
        genres_df = pd.json_normalize(genres)
        AgGrid(
            data=genres_df,
            fit_columns_on_grid_load=True,
            height=len(genres_df) * 30 + 50,
            key="genres_grid",
        )


def add_genre():
    genres_service = GenreService()
    genres = genres_service.get_genres()
    st.header("Adicionar Gênero")
    name = st.text_input("Nome do Gênero:")

    if st.button('Adicionar'):
        existing_genres = [
            genre['name'].lower() for genre in genres
        ]
        if name.lower() in existing_genres:
            st.warning("Gênero já existente!")
        elif name:
            genres_service.create_genre(name)
            st.success(f"Gênero '{name}' adicionado com sucesso!")
            sleep(2)
            st.rerun()
        else:
            st.error("Por favor, insira um nome para o gênero.")


def update_genre():
    genres_service = GenreService()
    genres = genres_service.get_genres()
    st.header("Atualizar Gênero")

    genre_names = [genre['name'] for genre in genres]
    selected_genre_name = st.selectbox("Selecione o gênero a ser atualizado:", genre_names)

    if selected_genre_name:
        genre_id = next(genre['id'] for genre in genres if genre['name'] == selected_genre_name)
        new_name = st.text_input("Novo Nome do Gênero:", value=selected_genre_name)

        if st.button('Atualizar'):
            if new_name and new_name != selected_genre_name:
                genres_service.update_genre(genre_id, new_name)
                st.success(f"Gênero '{selected_genre_name}' atualizado para '{new_name}' com sucesso!")
                sleep(2)
                st.rerun()
            else:
                st.error("Por favor, insira um novo nome para o gênero.")


def delete_genre():
    genres_service = GenreService()
    genres = genres_service.get_genres()
    st.header("Excluir Gênero")

    genre_names = [genre['name'] for genre in genres]
    selected_genre_name = st.selectbox("Selecione o gênero a ser excluído:", genre_names)

    if selected_genre_name:
        genre_id = next(genre['id'] for genre in genres if genre['name'] == selected_genre_name)

        if st.button('Excluir'):
            genres_service.delete_genre(genre_id)
            st.success(f"Gênero '{selected_genre_name}' excluído com sucesso!")
            sleep(2)
            st.rerun()
