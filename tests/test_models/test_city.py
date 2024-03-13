#!/usr/bin/python3
"""Module for City unittest."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittest for instantiation of the City class."""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        Ct = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(Ct))
        self.assertNotIn("state_id", Ct.__dict__)

    def test_name_is_public_class_attributes(self):
        Ct = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(Ct))
        self.assertNotIn("name", Ct.__dict__)

    def test_two_cities_unique_ids(self):
        Ct1 = City()
        Ct2 = City()
        self.assertNotEqual(Ct1.id, Ct2.id)

    def test_two_cities_different_created_at(self):
        Ct1 = City()
        sleep(0.05)
        Ct2 = City()
        self.assertLess(Ct1.created_at, Ct2.created_at)

    def test_two_cities_different_updated_at(self):
        Ct1 = City()
        sleep(0.05)
        Ct2 = City()
        self.assertLess(Ct1.updated_at, Ct2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_rep = rep(dt)
        Ct = City()
        Ct.id = "123456"
        Ct.created_at = Ct.updated_at = dt
        Ct_str = Ct.__str__()
        self.assertIn("[City] (123456)", Ct_str)
        self.assertIn("'id': '123456'", Ct_str)
        self.assertIn("'created_at': " + dt_rep, Ct_str)
        self.assertIn("'updated_at': " + dt_rep, Ct_str)

    def test_args_unused(self):
        Ct = City(None)
        self.assertNotIn(None, Ct.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        Ct = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(Ct.id, "354")
        self.assertEqual(Ct.created_at, dt)
        self.assertEqual(Ct.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests for save method of the City class."""

    @classmethod
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

    def test_one_save(self):
        Ct = City()
        sleep(0.05)
        first_updated_at = Ct.updated_at
        Ct.save()
        self.assertLess(first_updated_at, Ct.updated_at)

    def test_two_saves(self):
        Ct = City()
        sleep(0.05)
        first_updated_at = Ct.updated_at
        Ct.save()
        second_updated_at = Ct.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        Ct.save()
        self.assertLess(second_updated_at, Ct.updated_at)

    def test_save_with_arg(self):
        Ct = City()
        with self.assertRaises(TypeError):
            Ct.save(None)

    def test_save_updates_file(self):
        Ct = City()
        Ct.save()
        Ct_id = "City." + Ct.id
        with open("file.json", "r") as f:
            self.assertIn(Ct_id, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for to_dict method of the City class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        Ct = City()
        self.assertIn("id", Ct.to_dict())
        self.assertIn("created_at", Ct.to_dict())
        self.assertIn("updated_at", Ct.to_dict())
        self.assertIn("__class__", Ct.to_dict())

    def test_to_dict_contains_added_attributes(self):
        Ct = City()
        Ct.middle_name = "Holberton"
        Ct.my_number = "98"
        self.assertEqual("Holberton", Ct.middle_name)
        self.assertIn("my_number", Ct.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        Ct = City()
        Ct_dict = Ct.to_dict()
        self.assertEqual(str, type(Ct_dict["id"]))
        self.assertEqual(str, type(Ct_dict["created_at"]))
        self.assertEqual(str, type(Ct_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        Ct = City()
        Ct.id = "123456"
        Ct.created_at = Ct.updated_at = dt
        to_dict = {
                'id': '123456',
                '__class__': 'City',
                'created_at': dt.isoformat(),
                'updated-at': dt.isoformat(),
        }
        self.assertDictEqual(Ct.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        Ct = City()
        self.assertNotEqual(Ct.to_dict(), Ct.__dict__)

    def test_to_dict_with_arg(self):
        Ct = City()
        with self.assertRaises(TypeError):
            Ct.to_dict(None)


if __name__ == "__main__":
    unittest.main()
