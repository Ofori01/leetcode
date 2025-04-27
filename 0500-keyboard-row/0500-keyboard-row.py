class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')
        def check(word):
            if all(i.lower() in row1 for i in word):
                return True
            elif all(i.lower() in row2 for i in word):
                return True
            elif all(i.lower() in row3 for i in word):
                return True
            else:
                False

        return list(filter(check,words))
        