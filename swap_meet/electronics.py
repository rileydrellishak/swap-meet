from swap_meet.item import Item

class Electronics(Item):

    def __init__(self, id=None, type="Unknown"):
        super().__init__(id)
        self.type = type

    def get_category(self):
        return "Electronics"
    
    def __str__(self):
        return (f"An object of type {self.get_category()} with id {self.id}. "
        f"This is a {self.type} device.")
