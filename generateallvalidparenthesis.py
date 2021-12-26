def solve(string , A, open, close,ans):
    if len(string) == 2*A:
        # print(string)
        ans.append(string)
        return
    if open < A :
        solve(string+"(", A, open+1, close,ans)
    if close < open:
        solve(string+")", A, open, close+1,ans)
    return ans

def generateParenthesis(A):
    ans=[]
    string = ""
    ans = solve(string , A, 0, 0,ans)
    ans.sort()
    return ans

A=3
print(generateParenthesis(A))