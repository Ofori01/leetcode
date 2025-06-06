class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search for target or first 
        # were looking for first >=
        l,r = 0,len(nums)

        while l < r:

            mid = (l+r) // 2

            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l