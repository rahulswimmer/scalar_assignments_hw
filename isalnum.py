def solve(A):
    for i in A:
        if ((ord(i) not in range(65,91)) and (ord(i) not in range(97,123)) and (ord(i) not in range(48,58))):
            return 0
    return 1

A=[ "s", "g", "7", "A", "d", "v", "t", "W", "4", "A", "4", "2", "8", "f", "h", "B", "p", "h", "7", "0", "v", "q", "w", "9", "o" ]
print(solve(A))