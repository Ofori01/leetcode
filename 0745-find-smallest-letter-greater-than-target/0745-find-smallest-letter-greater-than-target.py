class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        # first ch greater than or equal
        # bisect right

        l,r = 0,len(letters)
        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        while l < r:
            mid = (l+r) // 2

            if letters[mid] <= target:
                l = mid + 1 
            else:
                r = mid
        return letters[r]