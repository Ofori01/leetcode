class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # use hashmap with seen counts

        

        sums = {0:1}

        cur,res = 0,0
        for r in nums:
            cur += r
            res += sums.get(cur-k,0)
            sums[cur]= 1+ sums.get(cur,0)
        return res

        