def solve(A):
    # sum = 0
    # for i in range(A+1):
    #     binFormat = bin(i)
    #     for j in binFormat:
    #         if j == '1':
    #             sum += 1
    # return sum
    arr = []
    arr.append(0)
    for i in range(1, A+1):
        arr[i] = arr[i/2]+i % 2

    print(arr)


A = 1
solve(A)
