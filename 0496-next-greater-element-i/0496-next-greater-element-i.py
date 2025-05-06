class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        check = {}
        stack = []
        for num in nums2:
            if not stack:
                stack.append(num)
            else:
                while stack and num > stack[-1]:
                    check[stack.pop()] = num
                stack.append(num)
        
        return [check[num] if num in check else -1 for num in nums1]
