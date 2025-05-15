# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l , r = 1,n

        while l < r:
            mid = (l + r) // 2

            # if bad it means mid to n is bad move r to mid-1
            if isBadVersion(mid):
                r =  mid

            # if not bad means 1 to mid not bad move l to mid +1
            else:
                l = mid + 1
        return l