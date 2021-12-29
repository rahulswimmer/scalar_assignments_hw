def solve(A):
    hashmap = {}
    ans = 0
    flag = True

    for i in range(len(A)):
        if A[i] in hashmap:
            hashmap[A[i]] += 1
        else:
            hashmap[A[i]] =  1

    for i in hashmap.values():
        if i > 1:
            flag = False
            ans = 

A=[1,1,3]
print(solve(A))