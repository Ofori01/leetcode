class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # sliding window won't work because of negetive numbers

        # use prefix sum with dict to check counts of times k sum was seen

        sums = {0:1}

        cur,res = 0,0
        for r in nums:
            cur += r
            res += sums.get(cur-k,0)
            sums[cur]= 1+ sums.get(cur,0)
        return res

        