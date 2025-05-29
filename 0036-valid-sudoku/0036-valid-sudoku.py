class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check grid rows and cols

        #  grid check
            # create grid
        grid  = defaultdict(list)

        for i,row in  enumerate(board):
            for j,ele in enumerate(row):
                if ele != '.':
                    if ele not in grid[i//3,j//3]:
                        grid[i//3,j//3].append(ele)
                    else:
                        return False
        print(grid)

        # row check

        for row in board:
            seen =set()
            for ele in row:
                if ele != '.':
                    if ele not in seen and ele!='.':
                        seen.add(ele)
                    else:
                        return False


        # col check

        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] != '.':
                    if board[row][col] not in seen and board[row][col] != '.' :
                        seen.add(board[row][col])
                    else:
                        return False
        return True



        