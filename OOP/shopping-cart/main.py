from product import Product
from inventory import Inventory

if __name__ == '__main__':
    p1 = Product('Apple', 0.67, 5)
    p2 = Product('Banana', 1.2, 15)
    
    #adding another apple with 10 qty
    p3 = Product('Apple', 0.67, 10)

    #add into inventory
    i1 = Inventory()
    i1.add_item(p1)
    i1.add_item(p2)
    i1.add_item(p3)

    #get the item details
    g1 = i1.get_item("Apple")
    g2 = i1.get_item("Banana")

    print(g1)#Apple - $0.67 (15 in stock)
    print(g2)#Banana - $1.20 (15 in stock)

    #print the total price
    total_price = i1.calculate_total_price()
    print(total_price)

