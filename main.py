from order import Order
from warehouse import Warehouse
import setup
from eventSystem import Event

[rows, columns, drones, deadline, maxLoad] = raw_input().split(" ")
raw_input() # ignore number of products
productWeights = [int(w) for w in raw_input().split(" ")]

warehouses = []
for w in range(int(raw_input())):
    [x, y] = [int(num) for num in raw_input().split(" ")]
    productAmount = [int(w) for w in raw_input().split(" ")]
    warehouses.append(Warehouse(x, y, productAmount))

orders = []
for c in range(int(raw_input())):
    [x, y] = [int(num) for num in raw_input().split(" ")]
    raw_input()
    products = [int(num) for num in raw_input().split(" ")]
    weight = 0
    for product in products:
        weight += productWeights[product]
    orders.append(Order(x, y, products, weight))

def getProductWeight(itemId):
    return productWeights[itemId]

events = {}
def registerEvent(turn, Event):
    if(turn not in events):
        events[turn] = []
    events[turn].append(Event)

def executeEvents(turn):
    if(turn not in events):
        return
    for e in events[turn]:
        e.callback()


sortedOrders = setup.sortOrders(orders)
for order in sortedOrders:
    ws =setup.getWarehousesByDistance(order.x, order.y, warehouses)
    for p in order.products:
        #TODO: find un-doable orders
        for w in ws:
            if(w.setDestination(p, order)):
                break

