import utils
from drone import Drone

class WarehouseObject(object):
    def __init__(self, productID):
        self.productID = productID
        self.destination = None

class Warehouse(object):
    
    def __init__(self, n, x, y, products):
        self.n = n
        self.x = x
        self.y = y
        self.products = [WarehouseObject(p) for p in products]
        self.potentialOrders = []

    def setDestination(self, productID, destination):
        for p in self.products:
            if(p.productID == productID and p.destination == None):
                p.destination = destination
                if(destination not in self.potentialOrders):
                    self.potentialOrders.append(destination)
                return True
        return False

    def loadDrone(self, drone, sort=True):
        if(len(self.potentialOrders) == 0):
            return not sort;
        if(sort):
            self.sortOrders()
        products = self.getProductsForOrder(self.potentialOrders[0])
        while(len(products) > 0):
            if(drone.canTake(products[0].productID)):
                p = products.pop(0)
                drone.load(p.productID, p.destination, self.n)
            else:
                return True;
        self.potentialOrders.pop(0)
        return True;
        #TODO: drone can take more - nearest neighbour search for next delivery

    def getProductsForOrder(self, order):
        return filter(lambda w: w.destination == order, self.products)

    def sortOrders(self):
        self.potentialOrders.sort(key=lambda o: self.getFitnessForOrder(o), reverse=True)

    def getFitnessForOrder(self, order):
        #TODO
        return -utils.squaredDistance(order.x, order.y, self.x, self.y)


