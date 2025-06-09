class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """

        l,c,r=0,0,len(nums) -1
        #place all colors at right position

        while c <= r:
            if nums[c] == 0:
                nums[l],nums[c] = nums[c],nums[l]
                c+=1
                l+=1
            elif nums[c] == 1:
                c+=1
            else:
                nums[r],nums[c] = nums[c], nums[r]
                r-=1
        