class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search first number that equals or is less than x. since decimals are not included
        '''
        The trick to knwoing when to stop is to simulate up the last two then see what happens
        if l = mid when condition is true
        r would only start decreasing when mid is too large so we bring r to mid, because mid is too large but we also need the just large number
        now l would be on the minimum value possible and r would be on the value that would just be larger
        which means with 2 numbers where l would be minimum and r would be the just max. and the loop would never exit
        so just l  = mid + 1 and return l -1

        when doing l-1 always increase upper bound. as bisect r,l uses right as len(nums)
        '''
        l,r = 0, x
        if x== 1: return 1

        while r-l> 1:
            mid = (l+r)//2

            if mid * mid <= x:
                l = mid
            else:
                r = mid
        return l
        