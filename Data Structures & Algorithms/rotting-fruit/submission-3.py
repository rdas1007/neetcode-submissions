class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        time, count = 0, 0
        q = deque()
        visited = set()
        # fresh_count == 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])

                elif grid[r][c] == 1:
                    count += 1
        if count == 0:
            return 0
        elif len(q) == 0:
            return -1

        while q:
            print(len(q))
            for _ in range(len(q)):
                r, c = q.popleft()
                for x, y in directions:
                    dx = r + x
                    dy = c + y
                    if (dx<0 or dy<0 or dx>=rows or dy>=cols or (dx, dy) in visited):
                        continue
                    visited.add((dx, dy))
                    if grid[dx][dy] == 1:
                        grid[dx][dy] == 2
                        count -= 1
                        q.append([dx, dy])
            time += 1
        if count == 0:
            return time-1
        else:
            return -1


        