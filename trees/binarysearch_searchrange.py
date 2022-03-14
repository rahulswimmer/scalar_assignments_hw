class Solution:
    def solve(self, A,B):
        (l, r) = (0, len(A) - 1)
        result = -1
        ans=[]

        if len(A)==1:
            ans.append(0)
            ans.append(0)
            return ans

        while l<=r:
            m=(l+r)//2

            if B==A[m]:
                result=m
                r=m-1
            elif B<A[m]:
                r=m-1
            else:
                l=m+1
        ans.append(result)

        (l, r) = (0, len(A) - 1)

        while l<=r:
            m=(l+r)//2

            if B==A[m]:
                result=m
                l=m+1
            elif B<A[m]:
                r=m-1
            else:
                l=m+1
        ans.append(result)

        if len(ans)==0:
            ans.append(-1)
            ans.append(-1)
            return ans

        return ans


if __name__=='__main__':
    bs = Solution()
    A=[1]
    print(bs.solve(A,1))