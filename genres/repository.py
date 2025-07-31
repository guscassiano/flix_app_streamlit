import requests
import streamlit as st


class GenresRepository:

    def __init__(self):
        self.__base_url = "http://guzzcass.pythonanywhere.com/api/v1"
        self.__genres_url = f"{self.__base_url}/genres/"
        self.__headers = {
            "Authorization": f"Bearer {st.session_state.token}",
        }

    def get_genres(self):
        response = requests.get(
            self.__genres_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            st.logout()
            return None
        raise Exception(f"Error ao buscar os gêneros: {response.text} - Status code: {response.status_code}")

    def create_genre(self, genre):
        response = requests.post(
            self.__genres_url,
            headers=self.__headers,
            data=genre,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            st.logout()
            return None
        raise Exception(f"Erro ao adicionar gênero: {response.text} - Status code: {response.status_code}")

    def update_genre(self, genre_id, genre):
        response = requests.put(
            f"{self.__genres_url}{genre_id}/",
            headers=self.__headers,
            data=genre,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            st.logout()
            return None
        raise Exception(f"Erro ao atualizar gênero: {response.text} - Status code: {response.status_code}")

    def delete_genre(self, genre_id):
        response = requests.delete(
            f"{self.__genres_url}{genre_id}/",
            headers=self.__headers,
        )
        if response.status_code == 204:
            return True
        if response.status_code == 401:
            st.logout()
            return None
        raise Exception(f"Erro ao deletar gênero: {response.text} - Status code: {response.status_code}")
