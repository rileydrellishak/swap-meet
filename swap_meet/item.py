import uuid

class Item:
    
    def __init__(self, id=None, condition=0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition

    def get_category(self):
        '''Returns a string of the name of the class.
        Input: None (must be called on an instance of Item).
        Output: a string literal representing the name of the class.
        '''
        return "Item"
    
    def __str__(self):
        '''
        Stringify an Item using str()
        Input: None (must be called on an instance of Item).
        Output: a string literal of a description of the item type and id.
        '''
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        '''
        Returns a string literal describing the condition of the item.
        Input: None (must be called on an instance of Item).
        Output: a string literal representing a description of the condition on a scale from 0 to 5 (inclusive, floats or integers), 5 being the best condition.
        '''
        if 0 <= self.condition  < 1:
            return "Horrible!"
        elif 1 <= self.condition < 2:
            return "Bad"
        elif 2 <= self.condition < 3:
            return "Mid"
        elif 3 <= self.condition < 4:
            return "Good"
        elif 4 <= self.condition < 5:
            return "Really good"
        elif self.condition == 5:
            return "Mint!"
        