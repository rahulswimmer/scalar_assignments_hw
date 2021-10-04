def solve(A):
    prefixSumArr = []
    prefixSumArr.append(A[0])
    for i in range(1,len(A)):
        prefixSumArr.append(A[i]+prefixSumArr[i-1])

    print(prefixSumArr)

A=[7,5,3,7]
solve(A)