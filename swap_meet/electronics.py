from swap_meet.item import Item

class Electronics(Item):

    def __init__(self, id=None, type="Unknown", condition=0):
        super().__init__(id, condition)
        self.type = type

    def get_category(self):
        return "Electronics"
    
    def __str__(self):
        parent_summary = super().__str__()
        child_summary = f"This is a {self.type} device."
        return f"{parent_summary} {child_summary}"