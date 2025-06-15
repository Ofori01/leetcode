class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        from copy import deepcopy
        #make deepcopy and use that to make changes
        a= deepcopy(matrix)
        j = len(a[0]) -1
        for row in a:
            i=0
            while i < len(row):
                matrix[i][j] = row[i]
                i +=1
            j-=1
        