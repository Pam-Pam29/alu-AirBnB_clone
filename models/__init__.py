from models.engine.file_storage import FileStorage

storage = FileStorage()  # Create a single instance of FileStorage
storage.reload()  # Call reload to load existing data from the JSON file
