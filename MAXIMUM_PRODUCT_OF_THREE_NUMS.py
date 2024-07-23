class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()  
        a=nums[-1]
        b=nums[-2]
        c=nums[-3]
        x=nums[0]
        y=nums[1]
        return max(a*b*c,a*x*y)
