#!/usr/bin/python3
"""Module for FileStorage class."""
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Class for storing, serializing and deserializing data."""
    __file_path = "file.json"

    __objects = {}

    def new(self, obj):
        """Sets in the __objects dictionary with key of <obj class name>.id"""
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """Returns the __onjects dictionary."""
        return FileStorage.__objects

    def save(self):
        """Serializes the __objects to JSON file by __file_path."""
        objs = FileStorage.__objects
        obj_dict = {}
        for obj in objs.key():
            obj_dict[obj] = objs[obj].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file."""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    obj_dict = json.load(f)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls_name = eval(class_name)
                        instance = cls_name(**value)
                        FileStorage.__objects[key] = instance
                except FileNotFoundError:
                    return
