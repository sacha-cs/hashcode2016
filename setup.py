import random
import utils

def sortOrders(orders):
    for order in orders:
        fitness = fitnessOrder(order)
        order.setFitness(fitness)
    orders.sort(key=lambda order: order.fitness, reverse=False)
    return orders

def fitnessOrder(order):
    neededW = []
    neededProducts = order.products
    for w in order.warehouses:
        if len(neededProducts) == 0:
            break
        elif:
            wProducts = [p.productId for p in w.products]
            tempNeededProducts = neededProducts
            for neededP in neededProducts:
                if neededP in wProducts:
                    tempNeededProducts.remove(neededP)
                    wProducts.remove(neededP)
            neededProducts = tempNeededProducts
            neededW.append(w)
    fitness = 0
    for w in neededW:
        fitness += utils.squaredDistance(order.x, order.y, w.x, w.y)
    return order.weight * fitness

def getWarehousesByDistance(x, y, warehouses):
    warehouses.sort(key=lambda w: utils.distance(x, y, w.x, w.y), reverse=False)
    return warehouses
