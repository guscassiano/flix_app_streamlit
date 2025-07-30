import requests
import streamlit as st

from login.service import logout


class MoviesRepository:

    def __init__(self):
        self.__base_url = "http://localhost:8000/api/v1"
        self.__movies_url = f"{self.__base_url}/movies/"
        self.__headers = {
            "Authorization": f"Bearer {st.session_state.token}"
        }

    def get_movies(self):
        response = requests.get(
            self.__movies_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f"Erro ao buscar os filmes: {response.text} - Status Code: {response.status_code}")

    def create_movie(self, movie):
        response = requests.post(
            self.__movies_url,
            headers=self.__headers,
            data=movie,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f"Erro ao adicionar filme: {response.text} - Status Code: {response.status_code}")

    def update_movie(self, movie_id, movie):
        response = requests.put(
            f'{self.__movies_url}{movie_id}/',
            headers=self.__headers,
            data=movie,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            st.logout()
            return None
        raise Exception(f'Erro ao atualizar filme: {response.text} - Status code: {response.status_code}')

    def delete_movie(self, movie_id):
        response = requests.delete(
            f'{self.__movies_url}{movie_id}/',
            headers=self.__headers
        )
        if response.status_code == 204:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f"Erro ao deletar filme: {response.text} - Status Code: {response.status_code}")

    def get_movies_stats(self):
        response = requests.get(
            f'{self.__movies_url}stats/',
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None

        raise Exception(f"Erro ao buscar as estatísticas dos filmes: {response.text} - Status Code: {response.status_code}")
