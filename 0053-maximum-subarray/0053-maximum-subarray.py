class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # using kadane's algo
        # for each i, if ele extends the maximum sum +/-, if the ele is already larger then the max sum,discard sum and start with ele

        cur_sum = nums[0]
        max_sum = nums[0]

        for r in nums[1:]:
            cur_sum = max(r,r + cur_sum)
            max_sum= max(cur_sum,max_sum)
        return max_sum


        