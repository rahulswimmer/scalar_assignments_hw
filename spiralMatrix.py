def solve(A):
    arr=[[0 for i in range(A)] for i in range(A)]
    print("zero")
    print(arr)
    rowStart=0
    colStart=0
    rowEnd=A
    colEnd=A
    count=1
    while colStart <=colEnd and rowStart<=rowEnd:
        print("colStart:",colStart)
        print("colEnd:",colEnd)
        for c in range(colStart,colEnd):
            arr[rowStart][c]=count
            count+=1
        rowStart+=1
        print("first")
        print(arr)
        print("rowstart:",rowStart)
        print("rowEnd:",rowEnd)
        for r in range(rowStart,rowEnd):
            arr[r][colEnd-1]=count
            count+=1
        colEnd-=1
        print("second")
        print(arr)
        print("colStart:",colStart)
        print("colEnd:",colEnd)
        for c in range(colEnd-1,colStart-1,-1):
            arr[rowEnd-1][c]=count
            count+=1
        rowEnd-=1
        print("third")
        print(arr)
        print("rowStart:",rowStart)
        print("rowEnd:",rowEnd)
        for r in range(rowEnd-1,rowStart,-1):
            arr[rowStart][c]=count
            count+=1
        colStart+=1
        print("fourth")
        print(arr)
    return arr
   
A=3
print(solve(A))