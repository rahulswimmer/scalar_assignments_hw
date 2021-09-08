def ispalindrome(A):
    if len(A) < 2: return 1
    if A[0] != A[-1]: return 0
    return ispalindrome(A[1:-1])

print(ispalindrome("lolo"))