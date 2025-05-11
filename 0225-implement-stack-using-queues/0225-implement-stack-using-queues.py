class MyStack:

    def __init__(self):
        self.input = deque()
        self.output = deque()

    def push(self, x: int) -> None:
        if self.output:
            self.output.append(x)
        else:
            self.input.append(x)
        

    def pop(self) -> int:
        if self.input:
            while len(self.input) > 1:
                self.output.append(self.input.popleft())
            return self.input.popleft()
        elif self.output:
            while len(self.output) > 1:
                self.input.append(self.output.popleft())
            return self.output.popleft()

    def top(self) -> int:
        if self.input:
            return self.input[-1]
        elif self.output:
            return self.output[-1]
        

    def empty(self) -> bool:
        return len(self.input) == 0 and len(self.output) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()