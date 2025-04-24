class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res  = 0
        r= 0
        l=0
        while r < len(arr):
            while l < len(arr)-1 and arr[l] == arr[l+1]:
                l+=1
            while r < len(arr)-1 and( arr[r-1] > arr[r] < arr[r+1] or arr[r-1] < arr[r] > arr[r+1]):
                r+=1
            res = max(res,r-l+1)
            l =r
            r+=1
        return res




