import json
import os
from datetime import datetime
from models.base_model import BaseModel  # Import your model classes

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        json_obj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(json_obj, f)

    def reload(self):
        """Deserializes the JSON file to __objects, only if the file exists."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                json_obj = json.load(f)
                for key, value in json_obj.items():
                    class_name = value['__class__']
                    # Assuming that only BaseModel is being used; for a more flexible solution, you might need to handle more classes dynamically
                    cls = globals().get(class_name, None)
                    if cls:
                        obj = cls(**value)
                        self.__objects[key] = obj
