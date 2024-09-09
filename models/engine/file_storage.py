import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj.to_dict()

    def save(self):
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

def reload(self):
    try:
        with open(self.__file_path, "r") as f:
            data = json.load(f)
            print("Loaded data:", data)  # Add this line
            self.__objects = {}
            for obj_id, obj_data in data.items():
                print("Deserializing object:", obj_id, obj_data)  # Add this line
                obj = BaseModel(**obj_data)
                self.__objects[obj_id] = obj
    except FileNotFoundError:
        pass  
           
   
