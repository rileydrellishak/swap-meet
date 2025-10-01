from swap_meet.item import Item

class Clothing(Item):
    
    def __init__(self, id=None, fabric="Unknown", condition=0):
        super().__init__(id, condition)
        self.fabric = fabric

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        parent_summary = super().__str__()
        child_summary = f"It is made from {self.fabric} fabric."
        return f"{parent_summary} {child_summary}"