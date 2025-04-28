class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        res =float('inf')
        total = sum(beans)
        for i,v in enumerate(beans):
            res = min(res,total - ((n-i)*v))
        return res
        