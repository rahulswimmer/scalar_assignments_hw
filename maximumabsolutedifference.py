def solve(A):
    ans=0
    xi = []
    yi = []

    # for i in range(len(A)):
    #     for j in range(len(A)):
    #         if abs(A[i]-A[j])+abs(i-j) > ans:
    #             ans = abs(A[i]-A[j])+abs(i-j)

    for i in range(len(A)):
        xi.append(A[i]+i)

    for i in range(len(A)):
        yi.append(A[i]-i)

    for i in range(len(A)):
        ans = max(max(xi)-min(xi),max(yi)-min(yi))
    return ans

A=[1,3,-1]
print(solve(A))