import sys

def solve(A,B):
    hashmap={}
    min1=0
    min2=0

    for i in A:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i]=1

    for i in range(B):
        min1=min(hashmap.values())

    print(min1)
    

A='abcabbccd'
B=3
solve(A,B)