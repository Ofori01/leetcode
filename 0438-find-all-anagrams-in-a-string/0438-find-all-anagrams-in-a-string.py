from collections import Counter, defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # go through s with window size of p and check using counters
        p_check = Counter(p)
        s_check = defaultdict(int)
        n = len(p)
        l=0
        res = []
        for r in range(len(s)):
            s_check[s[r]] +=1
            if r - l + 1 > n:
                if s_check[s[l]] == 1:
                    s_check.pop(s[l])
                else:
                    s_check[s[l]]-=1
                l+=1
            if r-l +1 ==n and s_check == p_check:
                res.append(l)
        return res




        