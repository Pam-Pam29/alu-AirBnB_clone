from models import storage

class BaseModel:
    # ...

    def save(self):
        storage.new(self)
        storage.save()

    def __init__(self, *args, **kwargs):
        if not kwargs:
            # Create a new instance
            storage.new(self)
        super().__init__(*args, **kwargs)
