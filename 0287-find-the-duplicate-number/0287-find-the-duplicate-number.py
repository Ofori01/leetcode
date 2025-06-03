class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use set to keep track of seen num
        sett = set()

        for num in nums:
            if num in sett:
                return num
            sett.add(num)
        