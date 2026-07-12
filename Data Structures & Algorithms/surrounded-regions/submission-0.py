class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            if board[r][0] == 'O':
                q.append((r, 0))
            if board[r][cols-1] == 'O':
                q.append((r, cols-1))
        for c in range(cols):
            if board[0][c] == 'O':
                q.append((0, c))
            if board[rows-1][c] == 'O':
                q.append((rows-1, c))

        def capture(q):
            while q:
                r, c = q.popleft()
                if (r<0 or c<0 or r>=rows or c>=cols or board[r][c] != 'O'):
                    continue
                board[r][c] = 'T'
                for x, y in directions:
                    q.append((r + x, c + y))
        capture(q)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'