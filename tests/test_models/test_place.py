#!/usr/bin/python3
"""Module for Place class unittest."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittest for instantiation of the Place class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        Pl = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(Pl))
        self.assertNotIn("city_id", Pl.__dict__)

    def test_user_id_is_public_class_attribute(self):
        Pl = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(Pl))
        self.assertNotIn("user_id", Pl.__dict__)

    def test_name_is_public_class_attributes(self):
        Pl = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(Place))
        self.assertNotIn("name", Pl.__dict__)

    def test_description_is_public_class_attribute(self):
        Pl = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(Place))
        self.assertNotIn("description", Pl.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        Pl = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(Place))
        self.assertNotIn("number_rooms", Pl.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        Pl = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(Place))
        self.assertNotIn("number_bathrooms", Pl.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        Pl = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(Place))
        self.assertNotIn("max_guest", Pl.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        Pl = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(Place))
        self.assertNotIn("price_by_night", Pl.__dict__)

    def test_latitude_is_public_class_attribute(self):
        Pl = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(Place))
        self.assertNotIn("latitude", Pl.__dict__)

    def test_longitude_is_public_class_attribute(self):
        Pl = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(Place))
        self.assertNotIn("longitude", Pl.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        Pl = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(Place))
        self.assertNotIn("amenity_ids", Pl.__dict__)

    def test_two_places_unique_ids(self):
        Pl1 = Place()
        Pl2 = Place()
        self.assertNotEqual(Pl1.id, Pl2.id)

    def test_two_places_different_created_at(self):
        Pl1 = Place()
        sleep(0.05)
        Pl2 = Place()
        self.assertLess(Pl1.created_at, Pl2.created_at)

    def test_two_places_different_updated_at(self):
        Pl1 = Place()
        sleep(0.05)
        Pl2 = Place()
        self.assertLess(Pl1.updated_at, Pl2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_rep = rep(dt)
        Pl = Place()
        Pl.id = "123456"
        Pl.created_at = Pl.updated_at = dt
        Pl_str = Pl.__str__()
        self.assertIn("[Place] (123456)", Pl_str)
        self.assertIn("'id': '123456'", Pl_str)
        self.assertIn("'created_at': " + dt_rep, Pl_str)
        self.assertIn("'updated_at': " + dt_rep, Pl_str)

    def test_args_unused(self):
        Pl = Place(None)
        self.assertNotIn(None, Pl.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        Pl = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(Pl.id, "354")
        self.assertEqual(Pl.created_at, dt)
        self.assertEqual(Pl.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """Unittests for save method of the Place class."""

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
        Pl = Place()
        sleep(0.05)
        first_updated_at = Pl.updated_at
        Pl.save()
        self.assertLess(first_updated_at, Pl.updated_at)

    def test_two_saves(self):
        Pl = Place()
        sleep(0.05)
        first_updated_at = Pl.updated_at
        Pl.save()
        second_updated_at = Pl.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        Pl.save()
        self.assertLess(second_updated_at, Pl.updated_at)

    def test_save_with_arg(self):
        Pl = Place()
        with self.assertRaises(TypeError):
            Pl.save(None)

    def test_save_updates_file(self):
        Pl = Place()
        Pl.save()
        Pl_id = "Place." + Pl.id
        with open("file.json", "r") as f:
            self.assertIn(Pl_id, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for to_dict method of the Place class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        Pl = Place()
        self.assertIn("id", Pl.to_dict())
        self.assertIn("created_at", Pl.to_dict())
        self.assertIn("updated_at", Pl.to_dict())
        self.assertIn("__class__", Pl.to_dict())

    def test_to_dict_contains_added_attributes(self):
        Pl = Place()
        Pl.middle_name = "Holberton"
        Pl.my_number = "98"
        self.assertEqual("Holberton", Pl.middle_name)
        self.assertIn("my_number", Pl.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        Pl = Place()
        Pl_dict = Pl.to_dict()
        self.assertEqual(str, type(Pl_dict["id"]))
        self.assertEqual(str, type(Pl_dict["created_at"]))
        self.assertEqual(str, type(Pl_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        Pl = Place()
        Pl.id = "123456"
        Pl.created_at = Pl.updated_at = dt
        to_dict = {
                'id': '123456',
                '__class__': 'Place',
                'created_at': dt.isoformat(),
                'updated-at': dt.isoformat(),
        }
        self.assertDictEqual(Pl.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        Pl = Place()
        self.assertNotEqual(Pl.to_dict(), Pl.__dict__)

    def test_to_dict_with_arg(self):
        Pl = Place()
        with self.assertRaises(TypeError):
            Pl.to_dict(None)


if __name__ == "__main__":
    unittest.main()
