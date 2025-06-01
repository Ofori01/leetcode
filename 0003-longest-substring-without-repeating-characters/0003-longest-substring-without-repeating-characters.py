class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using last seen index would be cool
        l = 0
        res= 0
        check = {}
        for r in range(len(s)):
            if s[r] not in check:
                check[s[r]] =1
            else:
                while s[r] in check:
                    check.pop(s[l])
                    l+=1
                check[s[r]] =1
                
            res = max(r-l+1,res)
        return res