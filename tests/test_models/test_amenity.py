#!/usr/bin/python3
"""Defines unittest for Amenity class."""
import os
import unittest
import models
from datetime import datetime
from models.amenity import Amenity


class TestAmenity_instantaion(unittest.TestCase):
    """Unittest for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        amnty = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amnty.__dict__)

    def test_two_amenities_unique_ids(self):
        amnty1 = Amenity()
        amnty2 = Amenity()
        self.assertNotEqual(amnty1.id, amnty2.id)

    def test_two_amenities_different_created_at(self):
        amnty1 = Amenity()
        sleep(0.05)
        amnty2 = Amenity()
        self.assertLess(amnty1.created_at, amnty2.created_at)

    def test_two_amenities_different_updated_at(self):
        amnty1 = Amenity()
        sleep(0.05)
        amnty2 = Amenity()
        self.assertLess(amnty1.updated_at, amnty2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_rep = rep(dt)
        amnty = Amenity()
        amnty.id = "123456"
        amnty.created_at = amnty.updated_at = dt
        amnty_str = amnty.__str__()
        self.assertIn("[Amenity] (123456)", amnty_str)
        self.assertIn("'id': '123456'", amnty_str)
        self.assertIn("'created_at': " + dt_rep, amnty_str)
        self.assertIn("'updated_at': " + dt_rep, amnty_str)

    def test_args_unused(self):
        amnty = Amenity(None)
        self.assertNotIn(None, amnty.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Intantiation with kwargs test method."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        amnty = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(amnty.id, "345")
        self.assertEqual(amnty.created_at, st)
        self.assertEqual(amnty.updated, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest(unittest.TestCase):
        """Unittest for save method of the Amenity class."""

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
        amnty1 = Amenity()
        sleep(0.05)
        first_updated_at = amnty.updated_at
        amnty.save()
        self.assertLess(first_updated_at, amnty.updated_at)

    def test_two_saves(self):
        amnty = Amenity()
        sleep(0.05)
        first_updated_at = amnty.updated_at
        amnty.save()
        second_updated_at = amnty.updated_at
        self.assertLess(first_updated_at, second.updated_at)
        sleep(0.05)
        amnty.save()
        self.assertLess(second_updated_at, amnty.updated_at)

    def test_save_with_arg(self):
        amnty = Amenity()
        with self.assertRaises(TypeError):
            amnty.save(None)

    def test_save_updates_file(self):
        amnty = Amenity()
        amnty.save()
        amnty_id = "Amenity." + amnty.id
        with open("file.json", "r") as f:
            self.assertIn(amnty_id, f.read())


class TestAmenity_to_dict(unnittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_dict_types(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        amnty = Amenity()
        self.assertIn("id", amnty.to_dict())
        self.assertIn("created_at", amnty.to_dict())
        self.assertIn("updated_at", amnty.to_dict())

    def test_to_dict_contains_added_attributes(self):
        amnty = Amenity()
        amnty.middle_name = "Holberton"
        amnty.my_number = 98
        self.assertEqual("Holberton", amnty.middle_name)
        self.assertIn("my_number", amnty.to_dict())

    def test_to_dict_datetime_attributes_are_str(self):
        amnty = Amenity()
        amnty_dict = amnty.to_dict()
        self.assertEqual(str, type(amnty_dict["id"]))
        self.assertEqual(str, type(amnty_dict["created_at"]))
        self.assertEqual(str, type(amnty_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        amnty = Amenity()
        amnty.id = "123456"
        amnty.created_at = amnty.update_at = dt
        to_dict = {
                'id': '123456',
                '__class__': 'Amenity',
                'created_at': dt.isoformat(),
                'updated_at': dt.isofromat(),
        }
        self.assertDictEqual(amnty.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        amnty = Amenity()
        self.assertNotEqual(amnty.to_dict(), amnty.__dict__)

    def test_to_dict_wit_arg(self):
        amnty = Amenity()
        with self.assertRaises(TypeError):
            amnty.to_dict(None)


if __name__ == "__main__":
    unittest.main()
