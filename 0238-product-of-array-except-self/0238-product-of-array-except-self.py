class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 2 6 24
        # 4 12 24 24
        prod = []
        cur = 1
        for i in nums:
            prod.append(cur)
            cur*=i
        cur =1
        for i in range(len(nums)-1,-1,-1):
            prod[i]*= cur
            cur*=nums[i]
        return prod



        

        