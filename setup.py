import random
import numpy as np

def sortOrders(orders):
    for order in orders:
        fitness = fitnessOrder(order)
        order.setFitness(fitness)
    orders.sort(key=lambda order: order.fitness, reverse=False)
    return orders

def fitnessOrder(order):
    return order.weight

def getWarehousesByDistance(x, y, warehouses):
    warehouses.sort(key=lambda w: distance(x, y, w.x, w.y), reverse=False)
    return warehouses

def distance(x1, y1, x2, y2):
    return np.sqrt(np.square(x2-x1) + np.square(y2-y1))
