#!/usr/bin/python3
"""This module creates a Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity.

    Attributes:
        name (str): The name of amenity.
    """

    name = ""
