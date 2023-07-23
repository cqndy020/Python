class Product:
    def __init__(self, name: str, price: float, qty=0):
        self.name = name 
        self.price = price
        self.qty = qty

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.qty} in stock)"
    
    def get_total_price(self):
        return self.price * self.qty