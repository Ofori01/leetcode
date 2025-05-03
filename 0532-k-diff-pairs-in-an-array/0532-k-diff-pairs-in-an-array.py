class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # create a set of the numbers
        # then go through the nums check if num -k exist: if yes increase res and remove the num-k from the set 

        diffs = Counter(nums)
        res = 0

        for num in diffs.keys():

            if k == 0:
                if diffs[num] >= 2:
                    res+=1

            else:
                if (k + num) in diffs:
                    res+=1

        return res


        