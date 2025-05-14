class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # binary seach but use the concept of checking the nums mid as a peak if it is not take right sub array and do the same. could also take the left subarray and check same condition holds

        l,r = 0 , len(nums)-1

        while l < r:
            mid = (l+ r) // 2
            
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid +1
        return l

        