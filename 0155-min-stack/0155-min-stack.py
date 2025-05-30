class MinStack:

    def __init__(self):
        self.stack = []        

    def push(self, val: int) -> None:
        # keep val and min ele
        if self.stack:
            self.stack.append([val,min(val,self.stack[-1][1])])
        else:
            self.stack.append([val,val])
        
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()