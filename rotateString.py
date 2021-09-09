def solve(A,B):
    
    first = A[0 : len(A)-B] 
    second = A[len(A)-B : ]
    return second+first

A='nrsizekitrkpbkqxsmq'
B=56
print(solve(A,B))