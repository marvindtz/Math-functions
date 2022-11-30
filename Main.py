import numpy as np
import matplotlib.pyplot as plt
import math

xrange = np.arange(-10,11, 0.1)
y = []
f = input('Formel:')
#print('hello world')
for x in xrange: 
#    tup = (x,eval(f))
    y.append(eval(f))
    
print(y)
plt.plot(xrange,y)
plt.show()