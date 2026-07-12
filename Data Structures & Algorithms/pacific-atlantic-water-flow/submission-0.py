class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = [[False]*cols for _ in range(rows)]
        atl = [[False]*cols for _ in range(rows)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pacific, atlantic = deque(), deque()
        for r in range(rows):
            pacific.append([r, 0])
            atlantic.append([r, cols - 1])
        for c in range(cols):
            pacific.append([0, c])
            atlantic.append([rows - 1, c])
        
        def bfs(q, ocean):
            while q:
                r,c = q.popleft()
                ocean[r][c] = True
                for x, y in directions:
                    dr, dc = r+x, c+y
                    # print(dr, dc)
                    if (0>dr or dr>=rows or 0>dc or dc>=cols):
                        continue
                    elif (not ocean[dr][dc] and heights[dr][dc]>=heights[r][c]):
                        q.append([dr, dc])
        
        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        
        return res