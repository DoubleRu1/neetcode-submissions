class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        x, y = 0, 0
        word_len = len(word)
        m, n = len(board), len(board[0])
        visited = [[False]* n for _ in range(m)]
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        ans = False
        def backtrack(x,y,idx):
            nonlocal ans
            # print(idx)
            if idx == word_len:
                ans = True
                return
            for dx, dy in directions:
                if 0<=x+dx<m and 0<=y+dy<n and not visited[x+dx][y+dy] and word[idx] == board[x+dx][y+dy]:
                    visited[x+dx][y+dy] = True
                    # print(word[idx],x+dx,y+dy)
                    backtrack(x+dx,y+dy,idx+1)
                    visited[x+dx][y+dy] = False

        for i in range(m):
            for j in range(n):
                if not ans and word[0] == board[i][j]:
                    visited[i][j] = True
                    backtrack(i,j,1)
                    visited[i][j] = False
        return ans
