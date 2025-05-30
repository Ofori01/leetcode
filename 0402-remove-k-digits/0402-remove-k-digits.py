class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # if lesser pop and reduce

        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k-=1
            stack.append(digit)
        
        if k:
            stack = stack[:-k]
        res = ''.join(stack).lstrip('0')
        return res if res else '0'