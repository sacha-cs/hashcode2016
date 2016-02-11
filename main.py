class Warehouse(object):
    
    def __init__(self, x, y, products):
        self.x = x
        self.y = y
        self.products = products

class Customer(object):
    def __init__(self, x, y, orders):
        self.x = x
        self.y = y
        self.orders = orders

[rows, columns, drones, deadline, maxLoad] = raw_input()
raw_input() # ignore number of products
productWeights = [int(w) for w in raw_input()]

warehouses = []
for w in range(int(raw_input())):
    [x, y] = [int(num) for num in raw_input()]
    productAmount = [int(w) for w in raw_input()]
    warehouses.append(Warehouse(x, y, productAmount))

customers = []
for c in range(int(raw_input())):
    [x, y] = [int(num) for num in raw_input()]
    raw_input()
    orders = [int(num) for num in raw_input()]
    customers.append(Customer(x, y, orders))





