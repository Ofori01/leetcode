class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        left = [-1] * len(arr)
        right = [len(arr)] * len(arr)
        stack = []

        for i,value in enumerate(arr):

            while stack and arr[stack[-1]] >= value:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []

        for i in range(len(arr)-1,-1,-1):

            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        
        res = sum( (i-left[i]) * (right[i]-i) * v for i,v in enumerate(arr)) % ((10 ** 9)+7)
        return res
