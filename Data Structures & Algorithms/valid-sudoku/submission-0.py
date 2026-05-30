class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(list)
        col_dict = defaultdict(list)
        box = [[[] for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row_dict[i]:
                        return False
                    elif board[i][j] in col_dict[j]:
                        return False
                    elif board[i][j] in box[i//3][j//3]:
                        return False
                    row_dict[i].append(board[i][j])
                    col_dict[j].append(board[i][j])
                    box[i//3][j//3].append(board[i][j])
        return True
