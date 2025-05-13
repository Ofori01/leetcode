class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Alla recursion

        # base case
        # if n == 1, true
        # if n < 1 , false

        if n == 1:
            return True
        elif n < 1:
            return False
        return self.isPowerOfThree(n/3) 