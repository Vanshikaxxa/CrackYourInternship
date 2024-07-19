# Sort Colors

class Solution(object):
    def sortColors(self, nums):
        p0, p1 = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1
            elif nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
        return nums
    

class Solution(object):
    def sortColors(self, nums):
        i = 0
        for k in range(0,3):
            for j in range(len(nums)):
                if nums[j] == k:
                    nums[i],nums[j] = nums[j],nums[i]
                    i += 1
        return nums
    

class Solution(object):
    def sortColors(self, nums):
        l, r = 0, len(nums) - 1
        i = 0
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1



class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(0, n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums
    
