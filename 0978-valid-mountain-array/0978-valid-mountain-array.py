class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        i = 0
        # check increasing then decreasing

        while i < len(arr)-1 and arr[i] < arr[i+1]:
            i+=1
        if i == len(arr)-1 or i ==0:
            return False

        while i < len(arr)-1 and arr[i] > arr[i+1]:
            i+=1
        print(i)
        if i != len(arr)-1:
            return False
        return True

        