def solve(A,B,C):
    hashmap={}
    commonArr = []
    for i in A:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i] =1

    for i in range(len(B)):
        if B[i] in hashmap:
            commonArr.append(B[i])

    for i in range(len(B))

    return commonArr

A=[1,1,2]
B=[2,3]
C=[3]
print(solve(A,B,C))
