#!/usr/bin/python3
"""This module creates a Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a Review class.

    Attributes:
        place_id (str): The place id.
        user-id (str): User id.
        txt (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
