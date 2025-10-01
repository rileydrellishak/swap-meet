from swap_meet.item import Item

class Decor(Item):
    
    def __init__(self, id=None, width=0, length=0, condition=0):
        super().__init__(id, condition)
        self.width = width
        self.length = length

    def get_category(self):
        return "Decor"
    
    def __str__(self):
        parent_summary = super().__str__()
        child_summary = f"It takes up a {self.width} by {self.length} sized space."
        return f"{parent_summary} {child_summary}"