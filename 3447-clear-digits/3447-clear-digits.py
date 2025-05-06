class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for i in s:
            if i.isalpha():
                stack.append(i)
            elif stack:
                stack.pop()
        return ''.join(stack)

        