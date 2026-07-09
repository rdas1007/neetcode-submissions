class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def island(r, c):
            nonlocal rows, cols, directions
            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c]=='0'):
                return
            grid[r][c] = '0'
            for x, y in directions:
                island(r + x, c + y)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island(r, c)
                    islands += 1
        return islands
