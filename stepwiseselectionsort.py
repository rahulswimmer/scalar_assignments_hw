def solve(A):
    outputArr=[]
    for i in range(len(A)):
        k = i
        for j in range(i+1, len(A)):
            if A[k] > A[j]:
                k = j
        A[i], A[k] = A[k], A[i]
        outputArr.append(k)
    return outputArr[:len(outputArr)-1]

A=[6, 4, 3, 7, 2, 8]
solve(A)