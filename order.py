class Order(object):
    def __init__(self, x, y, products, weight, warehouses):
        self.x = x
        self.y = y
        self.products = products
        self.weight = weight
        self.fitness = -1
        self.warehouses = warehouses.sort(key=lambda w: distance(self.x, self.y, w.x, w.y), reverse=False)

    def setFitness(self, fitness):
        self.fitness = fitness
        
