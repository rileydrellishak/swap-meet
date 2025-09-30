import uuid

class Item:
    
    def __init__(self, id=None):
        self.id = uuid.uuid4().int if id is None else id

    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."

# def get_by_id(self, id):
# if the id given matches the id of an item in inventory, return the item
# if id given is not an item in inventory, return None