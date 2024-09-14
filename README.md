# AirBnB clone - The console 🏠🏠

# Description of the project

This project is a simple clone of the AirBnB website. The first stage implements a backend interface or console to manage program data (like shell). Console commands allow users to create, update, destroy objects, and manage file storage.

# The console - tasks
- Put in place a parent class (called BaseModel) to take care of the initialization, serialization, and deserialization of future instances.
- Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
- Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.
- Create the first abstracted storage engine of the project: File storage.
- Create all unit tests to validate all our classes and storage engine.

# Description of the command interpreter

The command interpreter helps us manage the objects of our project by:

- Creating a new object (e.g., a new User or a new Place).
- Retrieving an object from a file, a database, etc.
- Performing operations on objects (count, compute stats, etc.).
- Updating attributes of an object.
- Destroying an object.

## How to start the interpreter

```bash
./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  delete  destroy  exit  help  q  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) quit

$ python3 -m unittest discover tests

## How to use the interpreter
To use the interpreter, enter the following commands:

Creating a new object:
(hbnb) create <class_name>

Retrieving an Object
(hbnb) show <class_name> <object_id>

Performing operations on objects
(hbnb) all

Updating attributes of an object:
(hbnb) update <class_name> <object_id> <attribute_name> "<attribute_value>"

Destroying an object
(hbnb) destroy <class_name> <object_id>

Tests
To run all the tests, execute the following command:
$ python3 -m unittest discover tests

You can also run a single test by specifying the test file:
$ python3 -m unittest tests/test_models/test_city.py

Authors
Victoria Fakunle
Vincent Mugabo
