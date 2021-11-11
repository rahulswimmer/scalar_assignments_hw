def uniquePaths(A,B):
    total = A + B - 2
    k = A - 1;
    if k == 0:
        return 1
    top = 1
    bottom = 1
    for i in range(k):
        top *= total - i
        bottom *= i + 1

    return int(top / bottom)

A=2
B=2
print(uniquePaths(A,B))