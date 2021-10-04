def solve(A):
    count=0
    setArr = set(A)
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]+A[j] in setArr:
                count+=1
    return count

A=[3,4,2,6,7]
print(solve(A))