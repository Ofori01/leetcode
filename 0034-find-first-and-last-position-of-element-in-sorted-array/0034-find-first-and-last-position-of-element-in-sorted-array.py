class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find first and last occurance of something
        # better to use a function and call twice or write logic for first and last occurance

        def binarySearch(arr,left):
            l,r = 0, len(arr)-1
            res = -1

            while l <= r:
                mid  = (l+r)//2

                if arr[mid] < target:
                    l = mid + 1
                elif arr[mid] > target:
                    r= mid-1
                else:
                    res = mid
                    if left:
                        r = mid-1
                    else:
                        l= mid + 1
            return res
            
        return [binarySearch(nums,True), binarySearch(nums,False)]
       

        