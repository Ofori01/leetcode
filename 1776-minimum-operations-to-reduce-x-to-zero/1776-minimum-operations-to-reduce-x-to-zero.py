class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # find sub array with sum = total -x. Since after removing x the subarray left would sum to total-x. using sliding window look for a sub array with this sum.


        # look for this subarray sum
        ans = sum(nums) -x
        n = len(nums)
        if ans == 0:
            return n
        l = 0
        cur_sum,res = 0,0

        for r in range(n):
            cur_sum += nums[r]

            while l < n and cur_sum > ans:
                cur_sum -= nums[l]
                l+=1
            if cur_sum == ans:
                res = max(res,r-l+1)
        
        if not res:
            return -1
        return n - res

