import uuid

class Item:
    
    def __init__(self, id=None):
        self.id = uuid.uuid4().int if id is None else id

    def get_category(self):
        return self.__class__.__name__
    
# def get_by_id(self, id):
# if the id given matches the id of an item in inventory, return the item
# if id given is not an item in inventory, return None