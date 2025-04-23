class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using last seen index would be cool
        # for every ch store it's seen index
        # if ch is seen again move l to last seen + 1
        # last seen did not work...unto legacy

        # l =0
        # res =0
        # last_seen = {}

        # for r in range(len(s)):
        #     if s[r] in last_seen:
        #         while l <= last_seen[s[r]]:
        #             last_seen.pop(s[l])
        #             l+=1
        #     last_seen[s[r]] = r
        #     print(last_seen,l)
        #     res = max(res, r-l + 1)
        # return res
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