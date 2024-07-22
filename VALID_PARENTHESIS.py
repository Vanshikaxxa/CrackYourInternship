class Solution(object):
    def isValid(self, s):
        hashmap={'(':')','{':'}','[':']'}
        stack=[]
        for char in s:
            if char in hashmap.keys():
                stack.append(char)
            elif char in hashmap.values():
                if not stack or hashmap[stack.pop()]!=char:
                    return False
            else:
                return False
        return len(stack) == 0
