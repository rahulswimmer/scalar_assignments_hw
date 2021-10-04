def solve(A,K):
    hashmap={}
    for i in A:
        if i%K in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i]=1
    print(hashmap)

    for i in hashmap:
        if hashmap[0]>=2

A=[3,7,5,5,4,6,1]
K=8
solve(A,K)