from utils import getProductWeight

class Drone(object):
    def __init__(self, x, y, maxLoad):
        self.x = x
        self.y = y

        self.inventory = []
        self.weightLeft = maxLoad

    def canTake(self, product):
        return getProductWeight(product) <= self.weightLeft

    def load(self, products):
        for p in products:
            self.weightLeft -= getProductWeight(p)
            self.inventory.append(p)

    def unload(self, products):
        for p in products:
            self.inventory.remove(p)
            self.weightLeft += getProductWeight(p)

    def move(self, x, y):
        self.x = x
        self.y = y 

