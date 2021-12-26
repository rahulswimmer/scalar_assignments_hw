def solve( A):
    hashmap = {}
    ans = []

    for i in range(len(A)):
        if A[i] in hashmap:
            hashmap[A[i]]+=1
        else:
            hashmap[A[i]]=1

    for i in hashmap:
        if hashmap[i]==1:
            ans.append(i)
    
    return ans

A=[ 186, 256, 102, 377, 186, 377 ]
print(solve(A))
    
