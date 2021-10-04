def arrange(A,B):
    hashmap={}

    for i in range(len(B)):
        if B[i] in hashmap:
            hashmap[B[i]]+=1
        else:
            hashmap[B[i]]=1

    for i in hashmap:
        if hashmap[i] % A != 0:
           return 0
        return 1

A=1
B="bc"
print(arrange(A,B))