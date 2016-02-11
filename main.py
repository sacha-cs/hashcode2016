from order import Order
from warehouse import Warehouse
import setup
from eventSystem import Event
from drone import Drone    
import utils
import math

[rows, columns, noOfDrones, deadline, maxLoad] = [int(num) for num in raw_input().split(" ")]
raw_input() # ignore number of products
utils.productWeights = [int(w) for w in raw_input().split(" ")]

warehouses = []
warehouseByPos = {}
for n in range(int(raw_input())):
    [x, y] = [int(num) for num in raw_input().split(" ")]
    productAmount = [int(w) for w in raw_input().split(" ")]
    products = []
    for i in range(len(productAmount)):
        products += ([i] * productAmount[i]) 
    w = Warehouse(n, x, y, products)
    warehouses.append(w)
    warehouseByPos[x + y * columns] = w

drones = []
for i in range(noOfDrones):
    drones.append(Drone(i, warehouses[0].x, warehouses[0].y, maxLoad))

orders = []
for c in range(int(raw_input())):
    [x, y] = [int(num) for num in raw_input().split(" ")]
    raw_input()
    products = [int(num) for num in raw_input().split(" ")]
    weight = 0
    for product in products:
        weight += utils.getProductWeight(product)
    orders.append(Order(x, y, products, weight))

currentTurn = 0;
events = {}
def registerEvent(turn, Event):
    if(turn not in events):
        events[turn] = []
    events[turn].append(Event)

def executeEvents(turn):
    if(turn not in events):
        return
    for e in events[turn]:
        e()

def addMoveToEvent(d, x, y, callback):
    distance = utils.distance(x, y, d.x, d.y)
    time = int(math.ceil(distance))
    registerEvent(currentTurn + time, lambda: callback)

def arrivedAt(d, dest):
    d.move(dest.x, dest.y)
    d.unload(dest)
    #TODO: go to other deliveries, but for now just go back to a warehouse
    ws = setup.getWarehousesByDistance(d.x, d.y, warehouses)
    registerEvent(currentTurn+1, lambda: addMoveToEvent(d, ws[0].x, ws[0].y, lambda: getOrderForDrone(d)))

def getOrderForDrone(d):
    warehouse = warehouseByPos[d.x + d.y * columns]
    warehouse.loadDrone(d)
    dest = d.getDestination()
    addMoveToEvent(d, dest.x, dest.y, lambda: arrivedAt(d, dest))
    


sortedOrders = setup.sortOrders(orders)
for order in sortedOrders:
    print order
    ws = setup.getWarehousesByDistance(order.x, order.y, warehouses)
    for p in order.products:
        print p
        #TODO: find un-doable orders
        for w in ws:
            if(w.setDestination(p, order)):
                print("Setting destination")
                break

for d in drones:
    registerEvent(0, lambda: getOrderForDrone(d))

for turn in range(deadline):
    currentTurn = turn
    executeEvents(turn)
