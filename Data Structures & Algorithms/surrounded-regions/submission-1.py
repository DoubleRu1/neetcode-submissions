class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        m, n = len(board), len(board[0])
        def dfs(x,y):
            nonlocal board
            for dx, dy in directions:
                i, j = x + dx, y + dy
                if 0<i<m-1 and 0<j<n-1 and board[i][j] == 'O':
                    board[i][j] = 'A'
                    dfs(i,j)
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][n-1] == 'O':
                dfs(i,n-1)
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0,j)
            if board[m-1][j] == 'O':
                dfs(m-1,j)
        print(board)
        for i in range(1,m-1):
            for j in range(1,n-1):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = "O"
        print(board)



