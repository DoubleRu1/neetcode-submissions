class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(-1,0),(0,-1),(1,0)]

        m,n = len(grid),len(grid[0])
        def dfs(i,j) -> int:
            count = 0
            for x,y in directions:
                x, y = x+i, j+ y
                if 0<=x<m and 0<=y<n and grid[x][y] == 1:
                    grid[x][y] = 0
                    count += dfs(x,y)
            return count + 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    ans = max(dfs(i,j),ans)
        return ans
