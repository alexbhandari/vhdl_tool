from entity import Entity

def paren(pin, value):
    return pin + '('+ str(value) + ')'

map = {'A':11,'B':8,'C':5,'D':2}
component = "g07_ADD3"
#First Blocks
name    = "Inst"+'A'+'1'
inputs  = {'x4':'GND',      'x3':'BIN(13)', 'x2':'BIN(12)', 'x1':'BIN(11)'}
outputs = {'y4':'ab( 9)',   'y3':'a(2)',    'y2':'a(1)',    'y1':'a(0)'}
print(Entity(name,component,inputs,outputs))
name    = "Inst"+'B'+'1'
inputs  = {'x4':'GND',      'x3':'a(9)', 'x2':'a(8)', 'x1':'a(7)'}
outputs = {'y4':'bc( 6)',   'y3':'a(2)',    'y2':'a(1)',    'y1':'a(0)'}
print(Entity(name,component,inputs,outputs))
name    = "Inst"+'C'+'1'
inputs  = {'x4':'GND',      'x3':'BIN(13)', 'x2':'BIN(12)', 'x1':'BIN(11)'}
outputs = {'y4':'cd( 2)',   'y3':'a(2)',    'y2':'a(1)',    'y1':'a(0)'}
print(Entity(name,component,inputs,outputs))
name    = "Inst"+'D'+'1'
inputs  = {'x4':'GND',      'x3':'BIN(13)', 'x2':'BIN(12)', 'x1':'BIN(11)'}
outputs = {'y4':'NOTHING',   'y3':'d(2)',    'y2':'d(1)',    'y1':'d(0)'}
print(Entity(name,component,inputs,outputs))

# Repeat Blocks

#A BLOCKS
for x in xrange(2,map['A']):
    name    = "InstA"+str(x)
    inputs  = { 'x4':paren('a',3*x-4),   'x3':paren('a',3*x-3),  'x2':paren('a',3*x-2),    'x1':paren('BIN',8-x) }
    outputs = { 'y4':paren('ab',10-x),   'y3':paren('a',3*x-1),  'y2':paren('a',3*x-2),    'y1':paren('a',3*x-3) }
    print(Entity(name,component,inputs,outputs))
    aNum = x
#B BLOCKS
for x in xrange(2,map['B']):
    name    = "InstB"+str(x)
    inputs  = { 'x4':paren('a',3*x-4),   'x3':paren('b',3*x-3),  'x2':paren('b',3*x-2),    'x1':paren('ab',8-x) }
    outputs = { 'y4':paren('bc',7-x),   'y3':paren('b',3*x-1),  'y2':paren('b',3*x-2),    'y1':paren('b',3*x-3) }
    print(Entity(name,component,inputs,outputs))
    bNum = x
#C BLOCKS
for x in xrange(2,map['C']):
    name    = "InstC"+str(x)
    inputs  = { 'x4':paren('c',3*x-4),   'x3':paren('c',3*x-3),  'x2':paren('c',3*x-2),    'x1':paren('BIN',8-x) }
    outputs = { 'y4':paren('cd',4-x),   'y3':paren('c',3*x-1),  'y2':paren('c',3*x-2),    'y1':paren('c',3*x-3) }
    print(Entity(name,component,inputs,outputs))
    cNum = x

#Last Blocks

x       = aNum + 1
name    = "InstA"+str(x)
inputs  = { 'x4':paren('a',3*x-4),   'x3':paren('a',3*x-3),  'x2':paren('a',3*x-2),    'x1':paren('BIN',8-x) }
outputs = { 'y4':'BCD2(0)',   'y3':'BCD1(3)',  'y2':'BCD1(2)',    'y1':'BCD1(1)' }
print(Entity(name,component,inputs,outputs))
x       = bNum + 1
name    = "InstB"+str(x)
inputs  = { 'x4':paren('a',3*x-4),   'x3':paren('b',3*x-3),  'x2':paren('b',3*x-2),    'x1':paren('ab',8-x) }
outputs = { 'y4':'BCD3(0)',   'y3':'BCD2(3)',  'y2':'BCD2(2)',    'y1':'BCD2(1)' }
print(Entity(name,component,inputs,outputs))
x       = cNum + 1
name    = "InstC"+str(x)
inputs  = { 'x4':paren('c',3*x-4),   'x3':paren('c',3*x-3),  'x2':paren('c',3*x-2),    'x1':paren('BIN',8-x) }
outputs = { 'y4':'BCD4(0)',   'y3':'BCD3(3)',  'y2':'BCD3(2)',    'y1':'BCD3(1)' }
print(Entity(name,component,inputs,outputs))
name    = "InstD"+'2'
inputs  = {'x4':'GND',      'x3':'BIN(13)', 'x2':'BIN(12)', 'x1':'BIN(11)'}
outputs = {'y4':'OVER',   'y3':'BCD4(3)',    'y2':'BCD4(2)',    'y1':'BCD4(1)'}
print(Entity(name,component,inputs,outputs))