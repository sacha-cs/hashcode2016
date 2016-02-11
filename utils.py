import math

productWeights = []

def getProductWeight(itemId):
    return productWeights[itemId]

def squaredDistance(x1, y1, x2, y2):
    return pow((x2-x1), 2) + pow((y2-y1),2)

def distance(x1, y1, x2, y2):
    return math.sqrt(squaredDistance(x1, y1, x2, y2))

