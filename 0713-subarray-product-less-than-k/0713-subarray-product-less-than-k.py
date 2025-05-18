class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # use sliding window technique and three pointers
        # slide and keep counting valid products

        res = 0
        product = 1
        l = 0
        if k <= 1:
            return 0

        for r in range(len(nums)):

            product *= nums[r]

            while l < len(nums) and  product >= k :
                product //= nums[l]
                l+=1
                
            res += r-l+1
        return res
