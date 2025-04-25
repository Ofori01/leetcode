class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # prefix sum with advanced jutsu
        prefix  = {0:1}
        res = 0

        # for each cur prefix check if prefix%k in prefix res + prefix count, add prefix[rem]+=1 to array

        cur = 0
        for i in nums:
            cur+=i
            res += prefix.get(cur%k,0)
            prefix[cur%k] = 1 + prefix.get(cur%k,0)
        return res

        