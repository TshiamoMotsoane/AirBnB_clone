#!/usr/bin/python3
"""This module creates a user class"""
from models.base_model import BaseModel


class city(BaseModel):
    """Defines a city class.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
