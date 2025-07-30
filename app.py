import streamlit as st

from actors.page import add_actor, show_actors, update_actor
from genres.page import add_genre, delete_genre, show_genres, update_genre
from home.page import show_home
from movies.page import add_movie, show_movies
from reviews.page import add_review, show_reviews
from login.page import show_login


def main():

    if 'token' not in st.session_state:
        show_login()
    else:
        st.title("Flix App")

        menu_option = st.sidebar.selectbox(
            "Selecione uma opção",
            ["Início", "gêneros", "Atores/Atrizes", "Filmes", "Avaliações"]
        )

        if menu_option == "Início":
            show_home()

        elif menu_option == "gêneros":
            show_genres()
            add_genre()
            update_genre()
            delete_genre()

        elif menu_option == "Atores/Atrizes":
            show_actors()
            add_actor()
            update_actor()

        elif menu_option == "Filmes":
            show_movies()
            add_movie()
        else:
            show_reviews()
            add_review()


if __name__ == "__main__":
    main()
