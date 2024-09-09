# models/__init__.py
from .engine import FileStorage

storage = FileStorage()
storage.reload()
