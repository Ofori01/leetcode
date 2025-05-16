class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        '''
        looking for consecutive elements to sum up to a k
        and get m groups of those
        since we have find an answer in a range of possibilities,binary search
        min= min(days), max  = max(days)
        create a possible function to determine whether chossen days would result in m bouquests produced
        '''
        # edge case if total number of flowers is less than m * k
        if len(bloomDay) < m*k:
            return -1
        def possible(days):
            bouquets = 0

            total_flowers =0

            for day in bloomDay:
                if day <= days:
                    total_flowers+=1
                else:
                    total_flowers = 0
                if total_flowers == k:
                    bouquets +=1
                    total_flowers = 0
            return  bouquets >= m
        
        # search space
        l,r = min(bloomDay), max(bloomDay)

        while l < r:

            mid = (l+r) // 2

            if possible(mid):
                r = mid
            else:
                l = mid + 1
        return l