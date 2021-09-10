def findAthFibonacci(self,A):
    if A == 0:
        return 0
 
    elif A == 1 or A == 2:
        return 1
 
    else:
        return findAthFibonacci(A-1) + findAthFibonacci(A-2)

print(findAthFibonacci(9))