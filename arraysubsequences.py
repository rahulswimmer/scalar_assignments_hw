def solve(A):
    start=0
    end=start+1

    while start < end:
        while end < len(A)-1:
            print(A[start],A[end])
            end+=1
        start+=1





A=[1,2,3]
solve(A)