class Solution(object):
    def longestCommonPrefix(self, strs):
        res=""
        strs.sort()
        first=strs[0]
        last=strs[-1]
        for i in range(len(first)):
            if first[i]!=last[i]:
                break
            res+=first[i]
        return(res)