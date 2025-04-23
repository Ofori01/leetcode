class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        cur = 0
        r= 0
        l=0

        while r < len(nums):
            cur+=nums[r]
            while cur >= target and l < len(nums):
                res = min(res,r-l+1)
                cur-=nums[l]
                l+=1
            r+=1
        return res if res != float('inf') else 0
