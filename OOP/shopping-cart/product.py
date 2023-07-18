class Product:
    def __init__(self, name, price, qty):
        self.name = name 
        self.price = price
        self.qty = qty

    def __str__(self):
        return f"{self.name} - ${self.price:2f} ({self.qty} in stock)"