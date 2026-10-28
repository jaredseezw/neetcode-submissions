class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Hastable in each row 
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        box = {i: set() for i in range(9)}
        for i in range(9):
            for j in range(9):
                boxnum = (i // 3) * 3 + (j // 3)
                num = board[i][j]
                if num == ".":
                    continue
                if num in rows[i] or num in cols[j] or num in box[boxnum]:
                    return False
                else:
                    rows[i].add(num)
                    cols[j].add(num)
                    box[boxnum].add(num)
        return True