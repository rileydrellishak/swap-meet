import uuid

class Item:
    
    def __init__(self, id=None, condition=0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition

    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition >= 0 and self.condition < 1:
            return "Horrible!"
        elif self.condition >= 1 and self.condition < 2:
            return "Bad"
        elif self.condition >= 2 and self.condition < 3:
            return "Mid"
        elif self.condition >= 3 and self.condition < 4:
            return "Decent"
        elif self.condition >= 4 and self.condition < 5:
            return "Pretty good"
        elif self.condition == 5:
            return "Mint!"