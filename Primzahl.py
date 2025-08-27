x = 1
y = 1000000
Teiler = [2,3,4,5,6,7,8,9]


for i in range(x,y):
    print(f'I: {i}')
    fl = 1
    while not fl == 0:
        for t in Teiler:
            fl = i % t
            print(fl)
    
print(i)