class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # base case: n == 1

        if n == 1:
            return True
        elif n < 1:
            return False
        n /= 4
        return self.isPowerOfFour(n)
        