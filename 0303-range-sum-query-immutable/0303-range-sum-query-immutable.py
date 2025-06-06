class NumArray:

    def __init__(self, nums: List[int]):
        # normal prefix sum
        prefix = []
        cur = 0
        for i in nums:
            cur+=i
            prefix.append(cur)
        self.prefix = prefix
        
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        else:
            return self.prefix[right] - self.prefix[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)