import numpy as np
# y = data[0] = Ax + N(y,y*s%)
# xi = i = data[i] + N(0,1) i=[1,N]
A = 2*np.pi
B = np.exp(1)
S = 5/100
# function gen(n,m,s)
def newData(i):
    X = i + np.random.rand()
    Y = (A*X+B)*(1+np.random.normal(loc=0,scale=S))
    with open("data.txt", "a") as f:
        f.write(f"{X}|{Y}\n")
def genListData(n):
    for i in range(n):
        newData(i)
def main():
    with open("data.txt","r+") as f:
        f.seek(0)
        f.truncate()
    n = int(input("Input size of data: "))
    genListData(n)
    print(f"New {n} linear data in 'data.txt'")
main()