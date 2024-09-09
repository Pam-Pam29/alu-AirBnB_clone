class BaseModel:
    _next_id = 1

    def __init__(self, *args, **kwargs):
        self.id = BaseModel._next_id
        BaseModel._next_id += 1
        # ...
