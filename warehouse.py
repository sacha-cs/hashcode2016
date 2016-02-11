import utils

class WarehouseObject(object):
    def __init__(self, productID):
        self.productID = productID
        self.destination = None

class Warehouse(object):
    
    def __init__(self, x, y, products):
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

    def getProductsForOrder(self, order):
        return filter(lambda wo: w.destination = order, products)

    def sortOrders(self):
        self.potentialOrders.sort(key=lambda o: self.getFitnessForOrder(o), reverse=True)

    def getFitnessForOrder(self, order):
        #TODO
        return -utils.squaredDistance(order.x, order.y, self.x, self.y)


