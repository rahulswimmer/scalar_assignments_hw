def containsDuplicate(nums):
    hashmap = {}
    flag=0
    
    for i in range(len(nums)):
        if nums[i] in hashmap:
            hashmap[nums[i]]+=1
        else:
            hashmap[nums[i]]=1
        
    for i in hashmap.values():
        if i > 1:
            flag=True
            break
        else:
            flag=False
    
    return flag
        
A=[1,2,3,4]
print(containsDuplicate(A))