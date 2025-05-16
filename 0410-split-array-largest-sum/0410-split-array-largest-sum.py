class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        '''
        so since answer is a sum we go through possibilities of sums with binary search.
        check whether with a max sum of sum the array can be split into k groups. 
        the search space will be the max num and the sum of the entire nums
        because for a k of say 3, a single number can stand alone and that and the minimum res is always the max number standing alone
        and the max res is all the numbers together.
        using this search space we can design a condition function that takes the potential res and checks whether it's possible to split

        so for the search space
        [F F F F F F T T T T T T]
        we're looking for the first true condtion. so even if a sum does not exist with the combination of numbers but results in a true split we know all sums above will also be true and find other trues on the left. we know that the first true will always be the answer
        '''

        def canSplit(possible_sum):
            total = 0
            count = 1

            for num in nums:
                total+= num
                if total > possible_sum:
                    total =num
                    count+=1
                if count > k:
                    return False
            return True
        
        # init search spce
        l,r = max(nums), sum(nums)

        while l < r:

            mid = (l+r) // 2

            if canSplit(mid):
                r = mid
            else:
                l = mid +1
        return l

        