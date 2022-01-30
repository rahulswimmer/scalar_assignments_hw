import sys

def solve(A,B):
    ans = []
    A.sort()

    for i in range(B):
        ans.append(A[i])


    return ans

A = [ 
       [26, 41],
  [40, 47],
  [47, 7],
  [50, 34],
  [18, 28]
     ]
B = 5
print(solve(A,B))