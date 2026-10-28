class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Hastable in each row 
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        box = {i: set() for i in range(9)}
        for i in range(9):
            for j in range(9):
                boxnum = (i // 3) * 3 + (j // 3)
                if board[i][j] in (rows[i] or cols[j] or box[boxnum]):
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    box[boxnum].add(board[i][j])
        return True