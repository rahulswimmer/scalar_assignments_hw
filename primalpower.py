def solve(A):
    count=0
    isprime=0
    for i in A:
        isprime=checkPrime(i)
        print(isprime)
        if isprime ==1 :
            count+=1
    return count

def checkPrime(n):
    if n > 1:
        for i in range(2,int(n/2)+1):
            if n%i==0:
                return 0
            return 1
    elif n==2:
        return 1
    else:
        return 0

A=[1,2,3,4,67]
print(solve(A))