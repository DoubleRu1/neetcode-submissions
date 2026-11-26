class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = []
        fresh_count = 0
        directions = [(-1,0),(0,1),(0,-1),(1,0)]


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        fc = 0
        layer = 0
        while q:
            temp = []
            for x, y in q:
                for dx, dy in directions:
                    dx = dx + x
                    dy = dy + y
                    if 0 <= dx < m and 0 <= dy < n:
                        if grid[dx][dy] == 1:
                            grid[dx][dy] = 2
                            temp.append((dx,dy))
                            fc += 1
            q = temp
            if q:
                layer += 1

        if fc != fresh_count:
            return -1
        return layer
                        