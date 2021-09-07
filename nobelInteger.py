def solve():
    inputArr = [3,2,1,3]
    ni=2
    count = 0

    for i in range(0,len(inputArr)):
        for j in range(0,len(inputArr)):
            if  inputArr[i]<inputArr[j]:
                count +=1
        if(count==inputArr[i]):
            return True
    return False




