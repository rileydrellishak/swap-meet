import uuid

class Item:
    
    def __init__(self, id=None):
        self.id = uuid.uuid4().int if id is None else id