from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        search space is speed between the min pile and max pile

        using a possibility function check if a speed is possible to eat withtin h time

        binary search the space using function to find the first true possibility
        '''

        def canFinish(speed):
            time = 0

            for pile  in piles:
                time+= ceil(pile/speed)

            if time > h:
                return False
            else:
                return True
        
        # init search space
        l,r = 1, max(piles)

        # go through search space, and binary searc first true
        while l < r:

            mid = (l+r) // 2

            if canFinish(mid):
                r = mid
            else:
                l = mid + 1
        return l

        