class Vendor:

    def __init__(self, inventory=None):
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
        '''
        This method finds and returns an item with a given id from the inventory list.
        Input: id of item to be returned from the inventory list
        Output: The item with the desired id. Returns None if the id given does not match any id of any item in the list.
        '''
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        '''
        Removes an item from Vendor inventory and adds it to another instance's inventory. Removes an item from other_vendor's inventory and adds it to the Vendor inventory.
        Inputs: other_vendor (an instance of Vendor), my_item (an instance of Item), their_item (an instance of Item)
        Outputs: Returns True if swap was successful, False if the input items are not already items in original inventories.
        '''
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.add(other_vendor.remove(their_item))
        other_vendor.add(self.remove(my_item))
        return True

    def swap_first_item(self, other_vendor):
        '''
        Swaps the first items of two lists of inventories.
        Inputs: other_vendor (an instance of Vendor)
        Output: Returns True after swapping the first items in two lists of vendor inventories. False if either itself or other_vendor has an empty inventory.
        '''
        if not self.inventory or not other_vendor.inventory:
            return False
        
        self.add(other_vendor.remove(other_vendor.inventory[0]))
        other_vendor.add(self.remove(self.inventory[0]))
        return True

    def get_by_category(self, category):
        '''
        Returns a list of item from inventory in a specific category
        Input : category of the item (string)
        Outputs: list of item in a specific category, Returns empty list if there is no item in the category.
        '''
        category_list = []
        for item in self.inventory:
            if item.get_category() == category:
                category_list.append(item)

        return category_list       
                
    def get_best_by_category(self, category):
        '''
        Returns a best item in a category
        Input : category of the item (string)
        Outputs: return item with best category, Returns None if there is no item in the category.
        '''
        highest_condition = 0
        best_category_item = None
        for item in self.inventory:
            if item.get_category() == category and item.condition > highest_condition:
                highest_condition = item.condition
                best_category_item = item
        return best_category_item        

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        '''
        Finds and swaps the best item of a certain category with another vendor.
        Inputs: other_vendor (an instance of Vendor), my_priority (a string representing the item category the user wants swapped into their inventory), their_priority (a string representing the item category the other vendor wants swapped into their inventory)
        Output: Returns True is swap was possible, False if Vendor has no item that matches their_priority category or other_vendor has no item that matches my_priority category.
        '''
        if (self.get_best_by_category(their_priority) is None or 
            other_vendor.get_best_by_category(my_priority) is None):
            return False
        
        vendor_receives = self.get_best_by_category(their_priority)
        other_vendor_receives = other_vendor.get_best_by_category(my_priority)

        self.swap_items(other_vendor, vendor_receives, other_vendor_receives)
        return True