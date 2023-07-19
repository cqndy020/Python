from product import Product

class Inventory:
    def __init__(self):
        self.products = {}
        
    def add_product(self, product):
        #check if the product in inventory exist 
        #increase qty if adding product is the same name with existing one
        existing_product = self.products.get(product.name)
        if existing_product:
            existing_product.qty += product.qty
        else:
            self.products[product.name] = product

    def get_product(self,name, price):
        return self.products.get(name, price)
    
    
