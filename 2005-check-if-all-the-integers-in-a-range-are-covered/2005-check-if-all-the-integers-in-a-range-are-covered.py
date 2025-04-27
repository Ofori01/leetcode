class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        check  = set()

        for a,b in ranges:
            for i in range(a,b+1):
                check.add(i)
        for i in range(left,right+1):
            if i not in check:
                return False
        return True
        