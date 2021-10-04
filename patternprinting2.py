def solve(A):
    arr=[]
    for i in range(1,A+1):
        col=[]
        for _ in range(A-i):
            col.append(0)
        for j in range(i,0,-1):
            col.append(j)
        arr.append(col)

    return arr

A=4
print(solve(A))