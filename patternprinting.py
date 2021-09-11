def solve(A):
    arr=[]
    for i in range(1,A+1):
        col=[]
        for j in range(1,i+1):
            col.append(j)
        for k in range(A-i):
                col.append(0)
        arr.append(col)

    return arr

A=2
print(solve(A))