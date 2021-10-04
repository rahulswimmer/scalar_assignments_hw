def solve(A, B):
    outputArr = [0]*A

    # 0(n2)
    # for i in range(len(B)):
    #     for j in range(B[i][0]-1, B[i][1]):
    #         outputArr[j] += B[i][2]

    # o(n)
    for i in range(len(B)):
        l = B[i][0]-1
        r = B[i][1]-1
        val = B[i][2]
        outputArr[l] += val
        # print(outputArr)
        # if r+1 < A:
        #     outputArr[r+1] -= val
    # for i in range(1, A):
    #     outputArr[i] += outputArr[i-1]
    return outputArr


A = 5
B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
print(solve(A, B))
