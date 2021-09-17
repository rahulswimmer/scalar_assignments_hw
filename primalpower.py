def solve(A):
    count=0
    isprime=0
    for i in A:
        isprime=checkPrime(i)
        if isprime ==1 :
            count+=1
    return count

def checkPrime(n):
    if n <=1:
        return 0
    else:
        for i in range(2,n):
            if n%i==0:
                return 0
        else:
            return 1

A=[1,2,3,4,67]
print(solve(A))