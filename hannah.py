print "Hello World"

x = 5

ys = [1, 2, 3]
for y in ys:
    print y

while x < 10:
    x += 1


def sayArg(x):
    print x

sayArg('boo')

d = {}

d['a'] = "A"

print d['a']

newy = [y * 2 for y in ys]

print newy[1:2]
