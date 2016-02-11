class Order(object):
    def __init__(self, x, y, products, weight):
        self.x = x
        self.y = y
        self.products = products
        self.weight = weight
        self.fitness = -1

    def setFitness(self, fitness):
        self.fitness = fitness
