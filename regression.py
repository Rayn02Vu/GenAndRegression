import numpy as np
import matplotlib.pyplot as plt
size = 0
X = np.asarray([])
Y = np.asarray([])
file = "data.txt"
with open(file,"r") as f:
    for line in f:
        size+=1
        x,y = line.rstrip().split("|")
        X = np.append(X,float(x))
        Y = np.append(Y,float(y))
a,b = np.polyfit(X,Y,1)
plt.plot(X,Y,'yo')
plt.plot(X,a*X+b)
print("Data size: ",size)
plt.show()


