import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str(self):
        my_model = BaseModel()
        expected_str = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(str(my_model), expected_str)

    def test_save(self):
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(my_model.updated_at, original_updated_at)

    def test_to_dict(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        dict_repr = my_model.to_dict()
        self.assertIsInstance(dict_repr, dict)
        self.assertIn("id", dict_repr)
        self.assertIn("created_at", dict_repr)
        self.assertIn("updated_at", dict_repr)
        self.assertIn("name", dict_repr)
        self.assertIn("my_number", dict_repr)
        self.assertIn("__class__", dict_repr)
        self.assertEqual(dict_repr["__class__"], "BaseModel")
        self.assertEqual(dict_repr["created_at"], my_model.created_at.isoformat())
        self.assertEqual(dict_repr["updated_at"], my_model.updated_at.isoformat())

if __name__ == "__main__":
    unittest.main()
