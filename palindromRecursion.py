def ispalindrome(A):
    if len(A) <= 1 :
      return 1
    if A[0] == A[len(A) - 1] :
        return ispalindrome(A[1:len(A) - 1])
    else :
        return 0

    

print(ispalindrome("lolol"))