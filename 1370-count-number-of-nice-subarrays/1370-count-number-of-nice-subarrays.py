class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cur,l,m,res = 0,0,0,0


        for r in range(len(nums)):
            cur += 1 if nums[r]&1 else 0
            while cur > k:
                cur-= 1 if nums[l]&1 else 0
                l+=1
                m = l
            if cur == k:
                while not nums[m] &1:
                    m+=1
                res += m-l+1
        return res
        