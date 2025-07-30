import streamlit as st
from api.service import Auth


def login(username, password):
    auth = Auth()
    response = auth.get_token(
        username=username,
        password=password
    )
    if response.get('error'):
        st.error(f"Erro ao realizar login: {response.get('error')}")
    else:
        st.session_state.token = response["access"]
        st.session_state.refresh = response["refresh"]
        st.success("Login realizado com sucesso!")
        st.rerun()


def logout():

    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()
