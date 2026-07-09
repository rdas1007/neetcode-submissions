class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        rows = len(grid) 
        cols = len(grid[0])
        area, maxArea = 0, 0

        def island(r, c):
            nonlocal area
            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c] == 0):
                return
            grid[r][c] = 0
            area += 1
            print(area)
            for x, y in directions:
                island(r+x, c+y)
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    island(r, c)
                    # print(area)
                    maxArea = max(area, maxArea)
                    area = 0
        return maxArea
