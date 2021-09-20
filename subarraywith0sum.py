def solve(A):
    sum = 0
    s = set()

    for i in range(len(A)):
        sum += A[i]

        if sum == 0 or sum in s:
            return 1
        s.add(sum)
    print(s)
 
    return 0

A=[1,2,3,6]
print(solve(A))