def solve(A):
    hashmap = {}
    oparr=[]
    for i in A:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    oparr.append(next(iter(hashmap)))

    for key,value in hashmap.items():
        i
    


    return oparr


A = [1, 2, 2, 5, 6]
print(solve(A))
