import streamlit as st
from reviews.repository import ReviewsRepository


class ReviewService:
    def __init__(self):
        self.reviews_repository = ReviewsRepository()

    def get_reviews(self):
        if 'reviews' in st.session_state:
            return st.session_state.reviews
        reviews = self.reviews_repository.get_reviews()
        st.session_state.reviews = reviews
        return reviews

    def create_review(self, movie_id, stars, comment):
        review = dict(
            movie=movie_id,
            stars=stars,
            comment=comment
        )
        new_review = self.reviews_repository.create_review(review)
        st.session_state.reviews.append(new_review)
        return new_review

    def update_review(self, review_id, stars, comment):
        review = dict(
            stars=stars,
            comment=comment
        )
        return self.reviews_repository.update_review(review_id, review)

    def delete_review(self, review_id):
        return self.reviews_repository.delete_review(review_id)
