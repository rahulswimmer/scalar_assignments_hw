def solve(A):
    hashmap = {}

    for i in A:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    return 1


A = [1, 2, 2, 5, 6]
print(solve(A))
