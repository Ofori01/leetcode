class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_total = 0
        l = 0
        res = float('inf')
        for i,num in enumerate(nums):
            cur_total+= num
            while cur_total >= target and l < len(nums):
                res= min(i-l+1,res)
                cur_total -= nums[l]
                l+=1
        return res if res != float('inf') else 0

        