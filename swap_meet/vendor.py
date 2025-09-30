class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        '''
        This method add an item to the inventory list.
        Input: item to be added to inventory
        Output: item added to the inventory

        '''
        self.inventory.append(item)
        return item
    def remove(self, item):
        '''
        This method removes an item from the inventory list.
        Input: item to be removed from the inventory.
        Output: Item which is removed, Return False if item not present.
        '''
        for position in range(len(self.inventory)):
            if self.inventory[position] == item:
                temp_variable = item
                self.inventory[position] = self.inventory[-1]
                self.inventory[-1] = item
                item_popped = self.inventory.pop(-1)
                return item_popped
        return False

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.add(other_vendor.remove(their_item))
        other_vendor.add(self.remove(my_item))
        return True




    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        self.add(other_vendor.remove(other_vendor.inventory[0]))
        other_vendor.add(self.remove(self.inventory[0]))
        return True

         

