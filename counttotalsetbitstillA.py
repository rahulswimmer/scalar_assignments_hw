def solve(A):
    sum = 0
    for i in range(A+1):
        binFormat = bin(i)
        for j in binFormat:
            if j == '1':
                sum += 1
    return sum


A = 1
print(solve(A))
