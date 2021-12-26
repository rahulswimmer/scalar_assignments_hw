def towerOfHanoi(A):
    ans=[]
    src=1
    dest=3
    temp=2
    solve(A,src,dest,temp,ans)
    return ans

def solve(A,src,dest,temp,ans):
    row=[]

    if A == 0:
        return
    solve(A-1,src,temp,dest,ans)
    row.extend((A,src,dest))
    solve(A-1,temp,dest,src,ans)
    
A=3
print(towerOfHanoi(A))