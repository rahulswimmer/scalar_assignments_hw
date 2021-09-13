def solve(A, B):
    hashmap = {}

    for i in A:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    for i in hashmap:
        if B-i in hashmap:
            if i*2 != B:
                return 1
            if i*2 == B and hashmap[i] > 1:
                return 1
    return 0


A = [1, 2, 2]
C = len(A)
B = 4
print(solve(A, B))
