def solve():
    # A = [1,2,2,1]
    # B = [2,3,1,2]

    # A = [2, 1, 4, 10]
    # B = [3, 6, 2, 10, 10]

    A = [ 17, 12, 5, 3, 14, 13, 3, 2 ]
    B = [ 19, 16, 8, 7, 12, 19, 10, 13, 8, 20, 16, 15, 4, 12, 3, 14, 14 ]
    commonElementArr = []
    arrAHash = {}

    for i in A:
        arrAHash[i]=A.count(i)

    for i in B:
        if i in arrAHash and arrAHash[i]>0:
            commonElementArr.append(i)
            arrAHash[i]-=1
            
solve()
    