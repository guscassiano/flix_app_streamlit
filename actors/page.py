from datetime import datetime
from time import sleep
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from actors.service import ActorService


def show_actors():
    actors_service = ActorService()
    actors = actors_service.get_actors()

    if actors:
        st.write("Lista de Atores/Atrizes: ")
        actors_df = pd.json_normalize(actors)
        AgGrid(
            data=actors_df,
            key="actors_grid",
            fit_columns_on_grid_load=True,
            height=len(actors_df) * 30 + 50
        )
    else:
        st.warning("Nenhum Ator/Atriz encontrado!")


def add_actor():
    actors_service = ActorService()
    actors = actors_service.get_actors()

    nationalities = actors_service.get_nationalities()
    nationality_options = [nat['name'] for nat in nationalities] if nationalities else []

    if not nationality_options:
        st.warning("Nenhuma nacionalidade encontrada.")
        return

    st.header("Adicionar Ator/Atriz")
    name = st.text_input("Nome do(a) Ator/Atriz:")
    birthday = st.date_input(
        label="Data de nascimento:",
        min_value="1900-01-01",
        max_value=datetime.today(),
        format="DD/MM/YYYY"
    )
    nationality = st.selectbox(
        label="Nacionalidade:",
        options=nationality_options,
        key="add_actor_nationality"
    )

    if st.button('Adicionar'):
        existing_actors = [
            actor['name'].lower() for actor in actors
        ]
        if name.lower() in existing_actors:
            st.warning("Ator já existente!")
        elif name and birthday and nationality:
            new_actor = actors_service.create_actor(name, birthday, nationality)
            if new_actor:
                st.success(f"Ator/Atriz '{name}' adicionado com sucesso!")
                st.rerun()
            else:
                st.error("Erro ao adicionar o Ator/Atriz.")
        else:
            st.error("Por favor, insira todos os dados solicitados do Ator/Atriz.")


def update_actor():
    actors_service = ActorService()
    actors = actors_service.get_actors()

    nationalities = actors_service.get_nationalities()
    nationality_options = [nat['name'] for nat in nationalities] if nationalities else []

    if not actors:
        st.warning("Nenhum Ator/Atriz encontrado para atualizar.")
        return

    if not nationality_options:
        st.warning("Nenhuma nacionalidade encontrada.")
        return

    st.header("Atualizar Ator/Atriz")
    actor_names = [actor['name'] for actor in actors]
    selected_actor_name = st.selectbox("Selecione o Ator/Atriz:", actor_names)

    if selected_actor_name:
        selected_actor = next(
            (actor for actor in actors if actor['name'] == selected_actor_name), None
        )
        if selected_actor:
            actor_id = next(actor['id'] for actor in actors if actor['name'] == selected_actor_name)
            new_name = st.text_input("Nome do(a) Ator/Atriz:", value=selected_actor['name'])
            new_birthday = st.date_input(
                label="Data de nascimento:",
                value=pd.to_datetime(selected_actor['birthday']).date(),
                min_value="1900-01-01",
                max_value=datetime.today(),
                format="DD/MM/YYYY"
            )

            current_nationality = selected_actor.get('nationality', '')
            default_index = 0
            if current_nationality and current_nationality in nationality_options:
                default_index = nationality_options.index(current_nationality)

            new_nationality = st.selectbox(
                label="Nacionalidade:",
                options=nationality_options,
                index=default_index,
                key="update_actor_nationality"
            )

            if st.button('Atualizar'):
                if (new_name != selected_actor['name'] or new_birthday != pd.to_datetime(selected_actor['birthday']).date() or new_nationality != current_nationality):
                    actors_service.update_actor(actor_id, new_name, new_birthday, new_nationality)
                    st.success("Ator/Atriz atualizado para com sucesso!")
                    sleep(2)
                    st.rerun()
                else:
                    st.warning("Nenhum dado deste Ator/Atriz foi alterado para ser atualizado.")
