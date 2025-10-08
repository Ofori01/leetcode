class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # solving using recursion
        
        # create helper function
        def helper(left: int, right: int)-> None:
            # base case
            if left >= right:
                return
            
            # other cases
            s[left], s[right] = s[right], s[left]
            
            helper(left+1, right-1)
        
        helper(0, len(s)-1)
