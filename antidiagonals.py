def solve(A,B):
    col = len(arr)
    row = 2 * col - 1
 
    outputArr = []
     
    for i in range(row) :
        outputArr.append([])
     
    for i in range(col) :
        for j in range(col) :
            outputArr[i + j].append(B[i][j])
    for i in range(len(outputArr)):
        for j in range(col-len(outputArr[i])):
            outputArr[i].append(0)
    return outputArr



      
A=3
count=1
arr=[[0 for i in range(A)] for i in range(A)]
for i in range(A):
        for j in range(A):
            arr[i][j]=count
            count+=1

print(solve(A,arr))