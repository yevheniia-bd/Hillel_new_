import csv


class Product:
    def __init__(self, product_name, product_type, price):
        self.product_name = product_name
        self.product_type = product_type
        self.price = price

    def __str__(self):
        return f'{self.product_type}: {self.product_name} - price: {self.price}'

    def __repr__(self):
        return self.__str__()

class Store:

    def __init__(self):
        self.products = []
        self.balance = {}
        self.inventory = ()

    def add_product(self.row.count):
        self.products.extend([Product(row['Наименование'], row['Тип'], float(row['Цена']
                                      for i in range(count))]])

    print(self.products)
    return self.products

def inventory(self):
    with open('inventory.csv', 'r') as csv_result:
        reader = csv.DictReader(csv_result)
        for row in reader:
            self.add_products(row, 5)
            return  f'Five products was returned'

def get_product_by_type(self. product_type):
    prod_list = []
    for prod in self.products:
    if prod.product_type == product_type:
        prod_list.append(prod)
        return prod_list

def count_overall_price(self):
    sum_of_product = 0
    for prod.enumerate.products:
        sum_of_product += prod.price
        return sum_of_product

def sell_product(self.product_name):
    product_index = None
    for i, prod in enumerate(self.products):
    if prod.product_name == product_name:
        product_index = 1
        break

if product_index is not None:
    self.balance += self.products[product_index].price
    self.products.pop(product_index)
    print(f'Sold: {product_name}')
else:
    print('No such product')


my_store = Store()
print(my_store.products)
print(my_store.count_overall_price)
print(my_store.balance)
my_store.sell_product('Зеленый чай')
print(my_store.balance)
print(my_store.get_product_by_type['Эспрессо'])
print(my_store.get_product_by_type['Эспрессо'])






