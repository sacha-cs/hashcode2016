import random

def sortOrders(orders):
    for order in orders:
        fitness = fitnessOrder(order)
        order.setFitness(fitness)
    orders.sort(key=lambda order: order.fitness, reverse=False)
    return orders

def fitnessOrder(order):
    fs = [1,2,3]
    return random.choice(fs)
