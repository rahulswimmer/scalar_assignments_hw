from typing import Hashable


def solve(A):
    hashmap={}
    countEven=0
    countOdd=0
    for i in A:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i] =1

    for i in hashmap:
        if hashmap[i]%2==0:
            countEven+=1
        else:
            countOdd+=1
    print(countEven)
    print(countOdd)
    if (countOdd==1 and countEven>=1) or countEven==len(A) or (countEven>=1 and countOdd==0) or (countEven==0 and countOdd==1):
        return 1
    return 0
    

A="vnpbeutxfqxriiajoejjmtjcx"
print(solve(A))
