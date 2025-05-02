class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        counts = defaultdict(int)
        l = 0


        for r in  range(len(nums)):
            counts[nums[r]] +=1
            if r - l > k:
                counts[nums[l]] -=1
                if counts[nums[l]] == 0:
                    # del counts[nums[l]]
                    counts.pop(nums[l])
                l+=1

            if counts[nums[r]] == 2:
                return True
        return False
            