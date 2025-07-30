import streamlit as st
from actors.repository import ActorsRepository


class ActorService:
    def __init__(self):
        self.actors_repository = ActorsRepository()

    def get_actors(self):
        if 'actors' in st.session_state:
            return st.session_state.actors
        actors = self.actors_repository.get_actors()
        st.session_state.actors = actors
        return actors

    def create_actor(self, name, birthday, nationality):
        actor = dict(
            name=name,
            birthday=birthday,
            nationality=nationality
        )
        new_actor = self.actors_repository.create_actor(actor)
        st.session_state.actors.append(new_actor)
        return new_actor

    def update_actor(self, actor_id, name, birthday, nationality):
        actor = dict(
            name=name,
            birthday=birthday,
            nationality=nationality
        )
        updated_actor = self.actors_repository.update_actor(actor_id, actor)
        for i, a in enumerate(st.session_state.actors):
            if a['id'] == actor_id:
                st.session_state.actors[i] = updated_actor
                break
        return updated_actor

    def delete_actor(self, actor_id):
        return self.actors_repository.delete_actor(actor_id)

    def get_nationalities(self):
        if 'nationalities' in st.session_state:
            return st.session_state.nationalities
        nationalities = self.actors_repository.get_nationalities()
        st.session_state.nationalities = nationalities
        return nationalities
