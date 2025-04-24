class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # for each s and t add diff to cur 
        # if cur !> maxcost keep increasing r
        # while cur > ... deduct cost of l  and l++
        cur,l,res= 0,0,0

        for r in range(len(t)):
            cur += abs(ord(s[r]) - ord(t[r]))

            while cur > maxCost:
                cur -= abs(ord(s[l]) - ord(t[l]))
                l+=1
            res = max(r-l+1,res)
        return res
            
        