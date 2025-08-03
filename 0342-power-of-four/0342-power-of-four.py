class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        # base case
        # 4 return 
        #  < 4 return false
        # recursion

        if n == 1 :
            return True
        elif n < 1 :
            return False
        n = n /4
        return self.isPowerOfFour(n)