import requests


class Auth:

    def __init__(self):
        self.__base_url = "http://localhost:8000/api/v1"
        self.__auth_url = f"{self.__base_url}/authentication/token/"

    def get_token(self, username, password):
        payload = {
            "username": username,
            "password": password
        }
        response = requests.post(self.__auth_url, json=payload)
        if response.status_code == 200:
            return response.json()
        return {"error": f"Error ao autenticar o usuário: {response.text}"}
