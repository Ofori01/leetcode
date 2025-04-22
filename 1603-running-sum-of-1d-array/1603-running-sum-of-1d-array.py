class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = []
        cur = 0
        for i in nums:
            cur+= i
            prefix.append(cur)
        return prefix

        