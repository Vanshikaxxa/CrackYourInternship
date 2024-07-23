class Solution(object):
    def climbStairs(self, n):
        if n<2:
            return 1
        else:
            return climbStairs(n-1)+climbStairs(n-2)
        
        