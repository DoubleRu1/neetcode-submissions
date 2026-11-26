class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(i,j):
            if dp[i][j] != -1:
                return dp[i][j]
            r = 0
            for dx, dy in directions:
                x, y = dx + i, dy + j
                if 0<=x<m and 0<=y<n and matrix[i][j] > matrix[x][y]:
                    r = max(dfs(x,y) + 1,r)
            dp[i][j] = r
            return r

        dfs(0,0)
        for i in range(m):
            for j in range(n):
                if dp[i][j] == -1:
                    dfs(i,j)
        mx = max(x for row in dp for x in row)
        return mx + 1