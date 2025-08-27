x = 1
y = 1000000
Liste = [2,3,4,5,6,7,8,9]


for i in range(x, y):
    for n in Liste:
        if i % n != 0:
            continue
        if i % n == 0:
            break
    