storage = {}  # Initialize an empty dictionary to store instances

def new(obj):
    """Stores a new instance in the storage"""
    storage[obj.id] = obj

def save():
    """Saves the current state of the storage"""
    # You can implement the saving logic here, e.g., to a file or database
    pass
