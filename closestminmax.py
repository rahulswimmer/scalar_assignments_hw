import sys

def solve(A):
    gmin=min(A)
    gmax=max(A)
    latestMin=sys.maxsize
    latestMax=-sys.maxsize-1
    ans=sys.maxsize

    for i in range(len(A)):
        if A[i]==gmin:
            latestMin=i
        elif A[i]==gmax:
            latestMax=i
        if A[i]==gmin and A[i]==gmax:
            ans=1
        else:
            ans = min(ans,abs(latestMin-latestMax)+1)
    return ans

    

A=[4,4,4,4,4,4]
print(solve(A))