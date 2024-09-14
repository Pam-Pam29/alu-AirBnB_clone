#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    def __init__(self, file_path):
        self.file_path = file_path

    def reload(self):
        try:
            with open(self.file_path, 'r') as f:
                objdict = json.load(f)
        except FileNotFoundError:
            objdict = {}
        except json.JSONDecodeError:
            objdict = {}
        return objdict

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

   def reload(self):
    try:
        with open(self.file_path, 'r') as f:
            objdict = json.load(f)
    except FileNotFoundError:
        print("Error: The JSON file doesn't exist.")
        objdict = {}
    except json.JSONDecodeError as e:
        print(f"Error: The JSON file is not properly formatted. {e}")
        objdict = {}
    return objdict
