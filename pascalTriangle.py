import math

def solve(A):
    arr=[]
    for i in range(A):
        col=[]
        for j in range(i+1):
            col.append(math.factorial(i)//(math.factorial(j)*math.factorial(i-j)))
            # print(math.factorial(i)//(math.factorial(j)*math.factorial(i-j)), end=" ")
        for k in range(A-i-1):
            col.append(0)
            # print("0",end=" ")
        arr.append(col)
        #print("")
    return arr

A=3
print(solve(A))