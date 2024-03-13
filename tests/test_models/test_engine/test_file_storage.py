#!/usr/bin/python3
"""Module for FileStorage unittest."""
import os
import json
import unittest
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittest fro instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is-private_str(self):
        self.assertEqual(str, type(FileStorage__file_path))

    def test_FileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittest for methods of the FileStorage class."""

    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        basemodel = BaseModel()
        usr = User()
        St = State()
        Pl = Place()
        Ct = City()
        amnty = Amenity()
        rev = Review()
        models.storage.new(basemodel)
        models.storage.new(usr)
        models.storage.new(St)
        models.storage.new(Pl)
        models.storage.new(Ct)
        models.storage.new(amnty)
        models.storage.new(rev)
        self.assertIn("BaseModel." + basemodel.id, models.storage.all().keys())
        self.assertIn(basemodel, models.storage.all().values())
        self.assertIn("User." + usr.id, models.storage.all().keys())
        self.assertIn(usr, models.storage.all().values())
        self.assertIn("State." + St.id, models.storage.all().keys())
        self.assertIn(St, models.storage.all().values())
        self.assertIn("Place." + Pl.id, models.storage.all.keys())
        self.assertIn(Pl, models.storage.all().values())
        self.assertIn("City." + Ct.id, models.storage.all().keys())
        self.assertIn(Ct, models.storage.all().values())
        self.assertIn("Amenity." + amnty.id, models.storage.all().keys())
        self.assertIn(amnty, models.storage.all().values())
        self.assertIn("Review." + rev.id, models.storage.all().keys())
        self.assertIn(rev, models.storage.all().values())

        def test_new_with_args(self):
            with self.assertRaises(TypeError):
                models.storage.new(BaseModel(), 1)

        def test_new_with_None(self):
            with self.assertRaises(AttributeError):
                models.storage.new(None)

        def test_save(self):
            basemodel = BaseModel()
            usr = User()
            St = State()
            Pl = Place()
            Ct = City()
            amnty = Amenity()
            rev = Review()
            models.storage.new(basemodel)
            models.storage.new(usr)
            models.storage.new(St)
            models.storage.new(Pl)
            models.storage.new(Ct)
            models.storage.new(amnty)
            models.storage.new(rev)
            save_text = ""
            with open("file.json", "r") as f:
                save_text = f.read()
                self.assertIn("BaseModel." + basemodel.id, save_text)
                self.assertIn("User." + usr.id, save_text)
                self.assertIn("State." + St.id, save_text)
                self.assertIn("Place." + Pl.id, save_text)
                self.assertIn("City." + Ct.id, save_text)
                self.assertIn("Amenity." + amnty.id, save_text)
                self.assertIn("Review." + rev.id, save_text)

        def test_save_with_arg(self):
            with self.assertRaises(TypeError):
                models.storage.save(None)

        def test_reload(self):
            basemodel = BaseModel()
            usr = User()
            St = State()
            Pl = Place()
            Ct = City()
            amnty = Amenity()
            rev = Review()
            models.storage.new(basemodel)
            models.storage.new(usr)
            models.storage.new(St)
            models.storage.new(Pl)
            models.storage.new(Ct)
            models.storage.new(amnty)
            models.storage.new(rev)
            objs = FileStorage._FileStorage__objects
            self.assertIn("BaseModel." + basemodel.id, objs)
            self.assertIn("User." + usr.id, objs)
            self.assertIn("State." + St.id, objs)
            self.assertIn("Place." + Pl.id, objs)
            self.assertIn("City." + Ct.id, objs)
            self.assertIn("Amenity." + amnty.id, objs)
            self.assertIn("Review." + rev.id, objs)

        def test_reload_with_arg(self):
            with self.assertRaises(TypeError):
                models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
