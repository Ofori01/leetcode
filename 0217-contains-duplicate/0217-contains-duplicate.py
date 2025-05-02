class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sett = set()

        for num in nums:
            if num not in sett:
                sett.add(num)
            else:
                return True
        return False
        