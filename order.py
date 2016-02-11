import utils

class Order(object):
    def __init__(self, n, x, y, products, weight, warehouses):
        self.n = n
        self.x = x
        self.y = y
        self.products = products
        self.weight = weight
        self.fitness = -1
        self.warehouses = sorted(warehouses, key=lambda w: utils.distance(self.x, self.y, w.x, w.y), reverse=False)

    def setFitness(self, fitness):
        self.fitness = fitness
        
