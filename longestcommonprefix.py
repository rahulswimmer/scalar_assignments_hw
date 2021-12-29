def solve(A):
	minlen = findMinLength(A)
	result =""
	for i in range(minlen):
	
		# Current character (must be same
		# in all strings to be a part of
		# result)
		current = A[0][i]

		for j in range(1,n):
			if (A[j][i] != current):
				return result

		# Append to result
		result = result+current

	return (result)

def findMinLength(A):
    min = len(A[0])
    for i in range(1,len(A)):
        if (len(A[i])< min):
            min = len(A[i])
    return(min)
	
A = ["geeksforgeeks", "geeks", "geek", "geezer"]
n = len(A)
print(solve(A))

