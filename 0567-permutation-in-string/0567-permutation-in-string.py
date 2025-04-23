from collections import Counter,defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        check = defaultdict(int)
        l= 0

        for r in range(len(s2)):
            check[s2[r]] += 1
            if r-l+1 > len(s1):
                if check[s2[l]] ==1:
                    check.pop(s2[l])
                else:
                    check[s2[l]] -=1  
                l+=1     
            if r-l+1 == len(s1):
                if check == s1_count:
                    return True
        return False


        