#!/usr/bin/python3
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Unit tests for the FileStorage class."""

    def setUp(self):
        """Set up the test environment."""
        self.storage = FileStorage()
        self.test_file = "test_file.json"
        self.storage._FileStorage__file_path = self.test_file  # Redirect to a test file

    def tearDown(self):
        """Clean up after the test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all(self):
        """Test the all() method."""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test the new() method."""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_save(self):
        """Test the save() method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        # Check if file is created and contains the correct data
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, 'r') as f:
            data = json.load(f)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, data)
        self.assertEqual(data[key]['id'], obj.id)

    def test_reload(self):
        """Test the reload() method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}  # Clear the current objects
        self.storage.reload()

        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].id, obj.id)

    def test_reload_no_file(self):
        """Test the reload() method when no file exists."""
        self.storage.reload()  # Should do nothing, no exceptions
        self.assertEqual(self.storage.all(), {})

    def test_datetime_conversion(self):
        """Test that BaseModel instances are correctly loaded with datetime conversion."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.storage.new(obj)
        self.storage.save()

        # Manually reload the data from the file
        with open(self.test_file, 'r') as f:
            data = json.load(f)

        # Convert datetime fields back to datetime objects
        loaded_obj_dict = data[f"BaseModel.{obj.id}"]
        self.assertEqual(loaded_obj_dict['created_at'], obj_dict['created_at'])
        self.assertEqual(loaded_obj_dict['updated_at'], obj_dict['updated_at'])

    def test_storage_singleton(self):
        """Test that storage is a singleton."""
        from models import storage
        self.assertIs(storage, self.storage)

if __name__ == '__main__':
    unittest.main()

