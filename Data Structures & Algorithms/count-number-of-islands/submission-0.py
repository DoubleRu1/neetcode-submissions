class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(i,j):
            for x,y in directions:
                x, y = x + i, y + j
                if 0<=x<m and 0<=y<n and grid[x][y] == '1':
                    grid[x][y] = '0'
                    dfs(x,y)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # print(grid)
                    grid[i][j] = '0'
                    dfs(i,j)
                    count += 1
        return count