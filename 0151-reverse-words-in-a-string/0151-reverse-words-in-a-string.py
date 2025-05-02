class Solution:
    def reverseWords(self, s: str) -> str:
        rev = s.split()

        return ' '.join(reversed(rev))
        