class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == '-':
                b,a= stack.pop(),stack.pop()
                stack.append(int(a)-int(b))
            elif i == '+':
                b,a= stack.pop(),stack.pop()
                stack.append(int(a)+int(b))
            elif i == '*':
                b,a= stack.pop(),stack.pop()
                stack.append(int(a)*int(b))
            elif i == '/':
                b,a= stack.pop(),stack.pop()
                stack.append(int(a)/int(b))
            else:
                stack.append(i)
            
        return int(stack[-1])
                
        