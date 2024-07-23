class Solution(object):
    def convertToTitle(self, columnNumber):
        column = {
            1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 
            11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 
            20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
        }
        s = ""
        if columnNumber <= 26:
            s = column[columnNumber]
        else:
            while columnNumber > 0:
                remainder = (columnNumber - 1) % 26
                s = column[remainder + 1] + s
                columnNumber = (columnNumber - 1) // 26
        return (s.upper())

                