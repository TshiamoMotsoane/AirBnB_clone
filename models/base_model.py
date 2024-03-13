#!/usr/bin/python3
"""This is a base model script"""

import uuid
import models
from datetime import datetime


class BaseModel:
    """BaseModel class defines common attributes and methods for other
    classes"""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance attributes

        Args:
            *args: list of arguments
            **kwargs: key-value arguments
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime
                        (kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime
                        (kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]


    def __str__(self):
        """Returns a string representation of the BaseModel instance."""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                self.__dict__)

    def save(self):
        """Updates the updated_at attribute with the current datetime."""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel instance"""

        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Return the print/str representation of BaseModel instance."""

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
