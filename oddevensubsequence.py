def solve():
    inputArr = [1, 2, 2, 5, 6]
    startIndex = 0
    lastIndex = startIndex+1
    subArrays = [[]]

    for i in range(len(inputArr)+1):
       for j in range(i):
           subArrays.append(inputArr[j:i])
    return subArrays
        


print(solve())
