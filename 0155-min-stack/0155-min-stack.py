class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        # before pushing check min val with val, if lesser or None append val with val, else append stack with val,minval
        minval = self.getMin()
        
        if minval==None or minval > val:
            self.stack.append([val,val])
        else:
            self.stack.append([val,minval])



        

    def pop(self) -> None:
        return self.stack.pop()[0] if self.stack else None
        

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None
        

    def getMin(self) -> int:
        # for every element keep track of the minimum up till it's insertion
        # for 5 8 4 3 6
        # [5,5] [8,5] [4,4] [3,3] [6,3]
        # return the top[1]. if not stack return None
        if self.stack:
            return self.stack[-1][1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()