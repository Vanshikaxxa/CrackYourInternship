def removeDuplicates(nums):
    li = [] 
    l, r = 0, 0
    while r < len(nums):
        while r < len(nums) and nums[l] == nums[r]:
            r += 1
        li.append(nums[l])
        l = r
    print(li)
removeDuplicates([1,1,2])
