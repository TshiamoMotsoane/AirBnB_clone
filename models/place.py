#!/usr/bin/python3
"""This module creates a place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place class.

    Attributes:
        city_id (str): The City id.
        user_id (str): User id.
        name (str): The name of the place.
        description (str): Description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): Number of bathrooms in the place.
        max_guest (int): The maximum number of guests in the place.
        price_by_night (int): The price by night.
        latitude (float): The latitude of the place.
        amenity_ids (list): Alist of Amenities.
    """

    city_id = ""
    user_id = ""
    name = ""
    descriptionn = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
