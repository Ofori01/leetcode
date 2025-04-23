class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum  = 0
        res = float('-inf')

        l = 0
        r = 0

        while r < len(nums):
            cur_sum += nums[r]
            if r-l+1 > k:
                cur_sum -= nums[l]
                l+=1
            if r-l+1 == k:
                res = max(res,cur_sum)

            r+=1
        return res/k
            
        