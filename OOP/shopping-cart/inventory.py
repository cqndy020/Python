from product import Product

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        #update the amount of item if you add the same name
        for existing_item in self.items:
            if existing_item.name == item.name:
                existing_item.qty += item.qty
                return existing_item
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return f"{item_name} is not in Inventory."

    #to calculate the total price in inventory
    def calculate_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.get_total_price()
        return f"The total price is ${total_price}"
    