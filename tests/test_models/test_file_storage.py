import unittest
from models.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def test_all(self):
        # Test 1: Test `all` method
        storage = FileStorage()
        obj1 = BaseModel()
        obj2 = BaseModel()
        storage.new(obj1)
        storage.new(obj2)
        all_objs = storage.all()
        self.assertEqual(len(all_objs), 2)
        self.assertIsInstance(all_objs, dict)
        self.assertIn(obj1.id, all_objs)
        self.assertIn(obj2.id, all_objs)

    def test_new(self):
        # Test 2: Test `new` method
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        self.assertIn(obj.id, storage.__objects)

    def test_save(self):
        # Test 3: Test `save` method
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        self.assertTrue(os.path.exists(storage.__file_path))
        with open(storage.__file_path, "r") as f:
            saved_data = json.load(f)
            self.assertIn(obj.id, saved_data)

    def test_reload(self):
        # Test 4: Test `reload` method
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        storage.reload()
        self.assertIn(obj.id, storage.__objects)

    def test_reload_multiple(self):
        # Test 5: Test `reload` with multiple objects
        storage = FileStorage()
        obj1 = BaseModel()
        obj2 = BaseModel()
        storage.new(obj1)
        storage.new(obj2)
        storage.save()
        storage.reload()
        self.assertIn(obj1.id, storage.__objects)
        self.assertIn(obj2.id, storage.__objects)

if __name__ == '__main__':
    unittest.main()
