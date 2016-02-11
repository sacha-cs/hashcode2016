from utils import getProductWeight

class Drone(object):
    def __init__(self, n, x, y, maxLoad):
        self.n = n
        self.x = x
        self.y = y

        self.inventory = {}
        self.weightLeft = maxLoad
        self.dests = []

    def getDestination(self):
        return self.dests[0]

    def canTake(self, product):
        return getProductWeight(product) <= self.weightLeft

    def load(self, p, dest, warehouseID):
        print self.n, 'L', warehouseID, p, 1
        if(dest not in self.inventory):
            self.inventory[dest] = []
            self.dests.append(dest)
        self.weightLeft -= getProductWeight(p)
        self.inventory[dest].append(p)

    def unload(self, dest):
        print self.n, 'D', dest.n, self.inventory[dest][0], 1
        for p in self.inventory[dest]:
            self.weightLeft += getProductWeight(p)
        del self.inventory[dest]

    def move(self, x, y):
        self.x = x
        self.y = y 
