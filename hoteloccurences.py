def solve(A):
    outputArr=[]

    for i in A:
        if i in outputArr:
            outputArr.remove(i)
            outputArr.append(i)
        else:
            outputArr.append(i)
    return outputArr

A=[1, 2, 3, 2, 5, 3, 2, 4]
print(solve(A))