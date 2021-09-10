def solve(A):
    for i in A:
        if ((ord(i) not in range(65,91)) and (ord(i) not in range(97,123))):
            return 0
    return 1

A="ScalarAcademy "
print(solve(A))