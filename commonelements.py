def solve():
    inputArr1 = [1,2,2,1]
    inputArr2 = [2,3,1,2]
    commonElementArr = []

    for i in range(len(inputArr1)):
        for j in range(i,len(inputArr2)) :
            if(inputArr1[i]==inputArr2[j]):
                print(inputArr1[i],inputArr2[j])
                commonElementArr.append(inputArr1[i])
                break
        continue
            
print(solve())
    