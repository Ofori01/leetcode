class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # sliding window way
        # move right and keep adding odds. 
        # if number of odds exceed. while, move a mid pointer till the count is up to the k
        # if the count == k: the ans + m-l + 1. baisically numbers between m and l. Because all those could have also formed a valid subarray

        l,r,m,count = 0,0,0,0
        res= 0

        for r in range(len(nums)):
            count += nums[r] & 1
            # if count exceeds
            while count > k:
                count -= nums[l] & 1
                l+=1
                m = l
            # if count reaches k
            if count == k:
                # move mid till count is no longer equal
                while not nums[m] & 1:
                    m+=1
                res+= m-l+1
        return res