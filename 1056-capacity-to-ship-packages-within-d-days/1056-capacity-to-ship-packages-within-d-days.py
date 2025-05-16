class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # realise that the search space is the capacities
        # the min capacity is max(weights) otherwise any lesser the ship can't take the largest weight
        '''
        the max capacity is the sum of all weights. where the ship takes everyone at once
        for every capacity between min and the max we need to find the min capacity that would get 5 days
        :) binary search, first True
        '''

        def possible(capacity):
            days_taken = 1
            total  = 0

            for weight in weights:
                total += weight
                
                if total > capacity:
                    total =weight
                    days_taken+=1
                
                if days_taken > days:
                    return False
            return True
        
        # binary search possiblilities
        # looking for minimum true possibility

        l,r = max(weights), sum(weights)

        while l < r:

            mid = (l + r) // 2

            if possible(mid):
                r = mid
            else:
                l = mid + 1
        return l
            
        