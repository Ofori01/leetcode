class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # will come back to this
        # stack = []
        # res =0

        # for p in s:
        #     if p == '(':
        #         stack.append(p)
        #     elif stack:
        #         res += 1 << (len(stack)-1)
        #         stack = []
        # return res
        # 

        # PUSH THE SCORES AND ON CLOSING UPDATE THE SCORE BY POPPING AND ADDING to the prev score
        stack = [0]

        for i in s:
            if i == '(':
                stack.append(0)
            else:
                score  = max(2*stack.pop(),1)
                stack[-1] +=score
        return stack.pop()
            
                
        