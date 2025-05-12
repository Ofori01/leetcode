class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

    #    since the k value is always in the middle and dosent have to be a contigious subarray, a direct check won't work.
    # using stack to keep track of the recent k that satisfies nums[k]<nums[j]. and looking for a num[i] that is nums[i] < nums[k]
    # a variable can keep track of the k that immediately satisfied the condition and on the next iteration check with the number
    # the stack is then replaced with the nums[j]. so if the previos k doesnt satisfy the i check, nums[j] would then be the new k to be used
    # until a valid nums k is found the stack would be piled up and nums_k would be -inf so the nums[i] comparison fails

        stack, nums_k = [],float('-inf')

        for num in reversed(nums):
            # nums[i] check
            if num < nums_k:
                return True
            
            while stack and stack[-1] < num:
                nums_k = stack.pop()
            stack.append(num)
        return False
            