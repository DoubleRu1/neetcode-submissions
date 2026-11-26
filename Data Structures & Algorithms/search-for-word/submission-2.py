class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = [[False] * n for _ in range(m)]
        def dfs(i,j,idx):
            if idx == len(word):
                return True
            accessable = False
            for dx, dy in directions:
                x = dx + i
                y = dy + j
                if 0<=x<m and 0<=y<n and board[x][y] == word[idx] and not visited[x][y]:
                    visited[x][y] = True
                    accessable = accessable or dfs(x,y,idx+1)
                    visited[x][y] = False
            return accessable
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j]=True
                    if dfs(i,j,1):
                        return True
                    visited[i][j] = False
        return False