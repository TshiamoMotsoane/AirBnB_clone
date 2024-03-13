#!/usr/bin/python3
"""Defines unittest for BaseModel class."""
import os
import unittest
import models
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantaion(unittest.TestCase):
    """Unittest for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))


    def test_two_models_unique_ids(self):
        basemodel1 = BaseModel()
        basemodel2 = BaseModel()
        self.assertNotEqual(basemodel1.id, basemodel2.id)

    def test_two_models_different_created_at(self):
        basemodel1 = BaseModel()
        sleep(0.05)
        basemodel2 = BaseModel()
        self.assertLess(basemodel1.created_at, basemodel2.created_at)

    def test_two_models_different_updated_at(self):
        basemodel1 = BaseModel()
        sleep(0.05)
        basemodel2 = BaseModel()
        self.assertLess(basemodel1.updated_at, basemodel2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_rep = rep(dt)
        basemodel = BaseModel()
        basemodel.id = "123456"
        basemodel.created_at = basemodel.updated_at = dt
        basemodel_str = basemodel.__str__()
        self.assertIn("[BaseModel] (123456)", basemodel_str)
        self.assertIn("'id': '123456'", basemodel_str)
        self.assertIn("'created_at': " + dt_rep, basemodel_str)
        self.assertIn("'updated_at': " + dt_rep, basemodel_str)

    def test_args_unused(self):
        basemodel = BaseModel(None)
        self.assertNotIn(None, basemode.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Intantiation with kwargs test method."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        basemodel = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(basemodel.id, "345")
        self.assertEqual(basemodel.created_at, st)
        self.assertEqual(basemodel.updated, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


class TestBaseModel_save(unittest(unittest.TestCase):
        """Unittest for save method of the BaseModel class."""

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
        basemodel1 = BaseModel()
        sleep(0.05)
        first_updated_at = basemodel.updated_at
        basemodel.save()
        self.assertLess(first_updated_at, .updated_at)

    def test_two_saves(self):
        basemodel = BaseModel()
        sleep(0.05)
        first_updated_at = basemodel.updated_at
        basemodel.save()
        second_updated_at = basemodel.updated_at
        self.assertLess(first_updated_at, second.updated_at)
        sleep(0.05)
        basemodel.save()
        self.assertLess(second_updated_at, basemodel.updated_at)

    def test_save_with_arg(self):
        basemodel = BaseModel()
        with self.assertRaises(TypeError):
            basemodel.save(None)

    def test_save_updates_file(self):
        basemodel = BaseModel()
        basemodel.save()
        basemodel_id = "BaseModel." + BaseModel.id
        with open("file.json", "r") as f:
            self.assertIn(basemodel_id, f.read())


class TestBaseModel_to_dict(unnittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_dict_types(self):
        self.assertTrue(dict, type(BaseModel().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        basemodel = BaseModel()
        self.assertIn("id", basemodel.to_dict())
        self.assertIn("created_at", basemodel.to_dict())
        self.assertIn("updated_at", basemodel.to_dict())

    def test_to_dict_contains_added_attributes(self):
        basemodel = BaseModel()
        basemodel.name = "Holberton"
        basemodel.my_number = 98
        self.assertIn("name", basemodel.to_dict())
        self.assertIn("my_number", basemodel.to_dict())

    def test_to_dict_datetime_attributes_are_str(self):
        basemodel = BaseModel()
        basemodel_dict = basemodel.to_dict()
        self.assertEqual(str, type(basemodel_dict["created_at"]))
        self.assertEqual(str, type(basemodel_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        basemodel = BaseModel()
        basemodel.id = "123456"
        basemodel.created_at = basemodel.update_at = dt
        to_dict = {
                'id': '123456',
                '__class__': 'Basemodel',
                'created_at': dt.isoformat(),
                'updated_at': dt.isofromat(),
        }
        self.assertDictEqual(basemodel.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        basemodel = BaseModel()
        self.assertNotEqual(basemodel.to_dict(), basemodel.__dict__)

    def test_to_dict_wit_arg(self):
        basemodel = BaseModel()
        with self.assertRaises(TypeError):
            basemodel.to_dict(None)


if __name__ == "__main__":
    unittest.main()
