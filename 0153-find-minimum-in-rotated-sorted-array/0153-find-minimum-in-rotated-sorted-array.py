class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search but keep moving towars the minimum
        l,r = 0, len(nums)-1

        while l < r :

            mid = (l+ r) //2
            # not numa[mid] > nums[mid +1]
            # because checking next elements may overshoot the current search space between r and l.... this does not check the ends if the minimum is located there. using right ensures the range is guaranteed to have the minimum since we know each subsequence is sorted in a way

            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r  = mid
            print(l,r,mid)
        return nums[l]
        