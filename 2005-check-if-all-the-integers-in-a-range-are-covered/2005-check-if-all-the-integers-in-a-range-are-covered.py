class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        #go though entire array and add it to a set
        #go through left and right and check if both the range is in the set
        covered = set()
        for start,end in ranges:
            covered.update(range(start,end+1))
        
        return all(num in covered for num in range(left,right+1))