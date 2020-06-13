class Product:
    def __init__(self, price, name, quantity):
        self.price = price
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return 'Produkt: {}, ilość: {}, cena: {}'.format(
            self.name, self.quantity, self.price
            )

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

    _iter_index = 0

    def __str__(self):
        s1 = 'Lista produktow w sklepie: \n'
        for x in self.products:
            s1 += 'Produkt: {}, cena: {}, ilość: {} \n'.format(
                self.products[x].get_name(), self.products[x].get_price(),
                self.products[x].get_quantity()
            )
        return s1

    def __len__(self):
        return len(self.products)

    def __iter__(self):
        return self

    def __next__(self):
        idx = self._iter_index
        if idx is None or idx >= len(self.products):
            self._iter_index = None
            raise StopIteration
        key_of_product = list(self.products)[idx]
        value = 'Produkt: {}, cena: {}, ilość: {}'.format(
            key_of_product, self.products[key_of_product].get_price(), 
            self.products[key_of_product].get_quantity())
        self._iter_index = idx + 1
        return value

    def buy(self, product_key):
        self.products[product_key].set_quantity(
            self.products[product_key].get_quantity() + 1
        )

    def sell(self, product_key):
        if(self.products[product_key].get_quantity() > 0):
            self.products[product_key].set_quantity(
                self.products[product_key].get_quantity() - 1
                )

    def get_total_price(self):
        sum = 0
        for x in self.products:
            sum += self.products[x].get_quantity() * self.products[x].get_price()
        return sum


product1 = Product(5.99, 'Grape', 25)
print(product1)

print('-'*20)

shop1 = Shop()
print(shop1)
print('Liczba produktów w sklepie: ', len(shop1), '\n')
print('Zakup jablka do sklepu...')
shop1.buy('Jablko')
print(shop1)

print('Sprzedaz dwoch ananasów...')
for x in range(0, 2):
    shop1.sell('Ananas')
print('Liczba produktów w sklepie: ', len(shop1),'\n')
print(shop1)

print('-'*20)

print('Całkowita cena wszystkich produktów w sklepie: ', shop1.get_total_price())
print('-'*20)
print('Działanie iteratora:')
myit = iter(shop1)
print(next(myit))
print(next(myit))