import requests
import streamlit as st

from login.service import logout


class ReviewsRepository:

    def __init__(self):
        # self.__base_url = 'https://guzzcass.pythonanywhere.com/api/v1'
        self.__base_url = "http://localhost:8000/api/v1"
        self.__reviews_url = f"{self.__base_url}/reviews/"
        self.__headers = {
            "Authorization": f"Bearer {st.session_state.token}"
        }

    def get_reviews(self):
        response = requests.get(
            self.__reviews_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f"Erro ao buscar as avaliações: {response.text} - Status Code: {response.status_code}")

    def create_review(self, review):
        response = requests.post(
            self.__reviews_url,
            headers=self.__headers,
            json=review
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f"Erro ao criar a avaliação: {response.text} - Status Code: {response.status_code}")

    def update_review(self, review_id, review):
        response = requests.put(
            f"{self.__reviews_url}{review_id}/",
            headers=self.__headers,
            json=review
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f"Erro ao atualizar a avaliação: {response.text} - Status Code: {response.status_code}")

    def delete_review(self, review_id):
        response = requests.delete(
            f"{self.__reviews_url}{review_id}/",
            headers=self.__headers,
        )
        if response.status_code == 204:
            return True
        if response.status_code == 401:
            logout()
            return False
        raise Exception(f"Erro ao deletar a avaliação: {response.text} - Status Code: {response.status_code}")
