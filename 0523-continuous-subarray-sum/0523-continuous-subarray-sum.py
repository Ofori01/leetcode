class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # prefix hash jujutsu with takashi storage and Insha Allah checking
        # store reminder of sum mod k as key and the sum as value
        # if the same reminder is seen, check cur_sum - value == the num. if it is then it means it's just one number in the subarray.
        # hope it works

        check = {0:-1}
        cur_sum = 0

        for i,num in enumerate(nums):
            cur_sum += num
            #  check divisibility
            rem = cur_sum % k
            if rem in check:
                if i - check[rem] > 1:
                    return True
            else:
                check[rem] = i
        return False

            


        