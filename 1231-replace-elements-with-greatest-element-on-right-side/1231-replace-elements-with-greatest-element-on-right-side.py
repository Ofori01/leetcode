class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greater = -1

        for i in range(len(arr)-1,-1,-1):
            num = arr[i]
            arr[i] = greater
            if num > greater:
                greater = num
        return arr
        