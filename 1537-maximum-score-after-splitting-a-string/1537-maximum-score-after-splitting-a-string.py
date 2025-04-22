class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count('1')
        zeros = 0
        res = 0
        for i in s[:-1]:
            if i == '0':
                zeros+=1
            else:
                ones-=1
            res = max(ones+zeros,res)
            
            
        return res