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

    def add.product(self.row.count):
        self.products.extend([Product[row['Наименование'], row['Тип'], float(row['Цена']
                                      for i in range(count)]]))

    print(self.products)
    return self.products

def inventory(self):
