class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        # base case
        # 4 return 
        #  < 4 return false

        if n == 1 :
            return True
        elif n < 1 :
            return False
        
        return self.isPowerOfFour(n / 4)