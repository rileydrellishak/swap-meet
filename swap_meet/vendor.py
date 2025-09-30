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

        # if item in self.inventory:
        #     self.inventory.remove(item)
        #     return item
        # else:
        #     return False   



