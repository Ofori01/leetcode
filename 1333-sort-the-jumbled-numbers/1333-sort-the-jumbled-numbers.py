class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def check(num):
            s  = str(num)
            temp =''
            for i in s:
                temp+=str(mapping[int(i)])
            return int(temp)

        nums.sort(key = check)
        return nums
        