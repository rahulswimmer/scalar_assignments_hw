def solve(A,B):
    outputarr=[[0 for i in range(2*(A))] for i in range(A)]
    print(outputarr)
    # for i in range(len(outputarr)):
    #     for j in range(len(outputarr))
      
A=3
count=1
arr=[[0 for i in range(A)] for i in range(A)]
for i in range(A):
        for j in range(A):
            arr[i][j]=count
            count+=1

solve(A,arr)