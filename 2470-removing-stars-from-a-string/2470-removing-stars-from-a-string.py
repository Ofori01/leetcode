class Solution:
    def removeStars(self, s: str) -> str:
        a = []

        for i in s:
            if i != "*":
                a.append(i)
            elif a:
                a.pop()

        return ''.join(a)