class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        res = ''
        ones= s.count("1")

        for i in range(len(s)):
            if i == len(s) - 1:
                res += '1'
            elif ones > 1:
                res+='1'
                ones-=1
            else:
                res += '0'
        return res