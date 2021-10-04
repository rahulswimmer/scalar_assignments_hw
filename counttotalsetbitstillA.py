class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 0:
            return 0
        elif A == 1:
            return 1

        x = self.largestPowerof2inrange(A)

        btill2x = x * (1 << (x-1))

        msb2xton = A - (1 << x) + 1

        rest = A - (1 << x)

        ans = btill2x + msb2xton + self.solve(rest)

        return ans%1000000007

    def largestPowerof2inrange(self, n):
        x = 0
        while (1 << x <= n):
            x += 1
        return x-1
