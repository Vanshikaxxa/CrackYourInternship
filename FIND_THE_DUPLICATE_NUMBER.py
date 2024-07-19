# Find the Duplicate Number
class Solution(object):
    def findDuplicate(self, nums):
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise] 
            hare = nums[nums[hare]]   
            if tortoise == hare:
                break
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return hare


class Solution(object):
    def findDuplicate(self, nums):
        set = {}
        for i in nums:
            if i in set:
                return i
            else:
                set[i] = 1
        return 0


class Solution(object):
    def findDuplicate(self, arr):
        seen = set()
        for num in arr:
            if num in seen:
                return num
            seen.add(num)
        return None
    

class Solution(object):
    def findDuplicate(self, nums):
        slow, fast = 0, 0
        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: 
                break
        slow2 = 0
        while True: 
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2: 
                return slow