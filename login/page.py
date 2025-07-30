import streamlit as st
from login.service import login


def show_login():
    st.title("Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if username and password:
            login(username, password)
        else:
            st.error("Por favor, preencha todos os campos.")
