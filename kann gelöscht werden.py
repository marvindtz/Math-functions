x = int(input('x:'))
y = int(input('y:'))

while x > 0 and y > 0:
    if x >= y:
        x = x - y
        print(f'x= {x}')
    else:
        y = y - x
        print(f'y= {y}')
print(f'ggt= {x + y}')
