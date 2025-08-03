class Solution:
    def isValid(self, s: str) -> bool:

        # just check end ones
        check = {
            '(' : ')',
            '[' : ']',
            '{':'}'
        }
        stack = []
        for i in s:
            if i in check:
                stack.append(i)
            else:
                if not stack:
                    return False
                
                if check[stack.pop()]!= i:
                    return False
        return len(stack) == 0
        #    }}}}} 
        
        