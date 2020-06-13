class Product:
    def __init__(self, price, name, quantity):
        self.price = price
        self.name = name
        self.quantity = quantity

    def get_price(self):
        return self.price
    
    def set_price(self, price):
        self.price = price
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
    
    def get_quantity(self):
        return self.quantity
    
    def set_quantity(self, quantity):
        self.quantity = quantity


class Shop:
    products = {'Jablko': Product(2.50, 'Jablko', 10), 'Ananas': Product(
        5.99, 'Ananas', 8
        )}

    def buy(self, product_key):
        self.products[product_key].set_quantity(
            self.products[product_key].get_quantity() + 1
            )

    def sell(self, product_key):
        self.products[product_key].set_quantity(
            self.products[product_key].get_quantity() - 1
            )

    def get_total_price(self):
        sum = 0
        for x in self.products:
            sum += self.products[x].get_quantity() * self.products[x].get_price()
        return sum


shop1 = Shop()
print(shop1.get_total_price())
shop1.buy('Jablko')
shop1.sell('Ananas')
print(shop1.get_total_price())

