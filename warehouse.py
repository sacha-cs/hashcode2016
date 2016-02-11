class WarehouseObject(object):
    def __init__(self, productID):
        self.productID = productID
        self.destination = None

class Warehouse(object):
    
    def __init__(self, x, y, products):
        self.x = x
        self.y = y
        self.products = [WarehouseObject(p) for p in products]

    def setDestination(self, productID, destination):
        for p in self.products:
            if(p.productID == productID and p.destination == None):
                p.destination = destination
                return True
        return False
