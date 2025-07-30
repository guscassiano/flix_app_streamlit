import requests
import streamlit as st

from login.service import logout


class ActorsRepository:

    def __init__(self):
        self.__base_url = "http://localhost:8000/api/v1"
        self.__actors_url = f"{self.__base_url}/actors/"
        self.__headers = {
            "Authorization": f"Bearer {st.session_state.token}",
        }

    def get_actors(self):
        response = requests.get(
            self.__actors_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            st.logout()
            return None
        raise Exception(f"Erro ao buscar os atores: {response.text} - Status code: {response.status_code}")

    def create_actor(self, actor):
        response = requests.post(
            self.__actors_url,
            headers=self.__headers,
            data=actor,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f"Erro ao adicionar ator: {response.text} - Status code: {response.status_code}")

    def update_actor(self, actor_id, actor):
        response = requests.put(
            f"{self.__actors_url}{actor_id}/",
            headers=self.__headers,
            data=actor,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            st.logout()
            return None
        raise Exception(f"Erro ao atualizar ator: {response.text} - Status code: {response.status_code}")

    def delete_actor(self, actor_id):
        response = requests.delete(
            f"{self.__actors_url}{actor_id}/",
            headers=self.__headers,
        )
        if response.status_code == 204:
            return True
        if response.status_code == 401:
            st.logout()
            return None
        raise Exception(f"Erro ao deletar ator: {response.text} - Status code: {response.status_code}")

    def get_nationalities(self):
        nationalities_url = f"{self.__base_url}/nationalities/"
        response = requests.get(
            nationalities_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f"Erro ao buscar nacionalidades: {response.text} - Status code: {response.status_code}")
