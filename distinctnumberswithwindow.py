def solve(A,B):
    hashmap={}
    for i in range(B):
        print(A[i])
    #     if A[i] in hashmap:
    #         hashmap[A[i]]+=1
    #     else:
    #         hashmap[A[i]]=1
    # return hashmap


A=[1, 2, 1, 3, 4, 3]
B=3
print(solve(A,B))
