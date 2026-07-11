class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def addCell(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] == -1):
                return
            visited.add((r, c))
            q.append((r, c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for x, y in directions:
                     addCell(r + x, c + y)
            dist += 1