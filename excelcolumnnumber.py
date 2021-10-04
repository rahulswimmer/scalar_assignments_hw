def solve(A):
    result = 0
    for i in range(len(A)):
        result *= 26;
        result += ord(A[i]) - ord('A') + 1
        print(result)
 
    return result

A="ABCD"
print(solve(A))