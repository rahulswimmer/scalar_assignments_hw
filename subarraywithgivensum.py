def solve(A,B):
    curr_sum = A[0]
    start = 0
    n = len(A)
    i = 1
    ans = []
    while i <= n:
        while curr_sum > B and start < i-1:
            curr_sum = curr_sum - A[start]
            start += 1
             
        if curr_sum == B:
            ans.append(start)
            ans.append(i-1)
            return ans
 
        if i < n:
            curr_sum = curr_sum + A[i]
        i += 1
 
    return -1

A=[ 5, 10, 20, 100, 105 ]
B=110
print(solve(A,B))