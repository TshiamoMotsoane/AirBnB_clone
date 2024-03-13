#!/usr/bin/python3
"""Defines a User class."""
from models.base_model import BaseModel


class User (BaseModel):
    """Represents a User class.

    Attributes:
        email (str): Email of the user.
        password (str): The password of the user.
        first_name (str): The first name if the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
