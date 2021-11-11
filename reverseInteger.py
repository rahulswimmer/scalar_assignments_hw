def solve(A):
    ans = 0
    flag=0

    if A < 0:
        A=A*(-1)
        flag=1

    while(A > 0):
        temp = A % 10
        ans = ans * 10 + temp
        A = A // 10

    if ans < -2147483648  or ans > 2147483647:
        return 0

    if flag==1:
        return (-1)*ans
    else:
        return ans

A=-1146467285
print(solve(A))