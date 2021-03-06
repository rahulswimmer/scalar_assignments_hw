import math

def solve(A):
    count=0
    isprime=0
    for i in A:
        isprime=checkPrime(i)
        if isprime ==1 :
            count+=1
    return count

def checkPrime(n):
    max_div = math.floor(math.sqrt(abs(n)))
    if n <=1:
        return 0
    else:
        for i in range(2,max_div+1):
            if n%i==0:
                return 0
        else:
            return 1

A=[-11, 7, 8, 9, 10, 11]
print(solve(A))