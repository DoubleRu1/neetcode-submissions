class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def dfs_pac(i: int,j: int,visited: list[list[bool]]):
            if i == m-1 or j == n-1:
                return True
            visit_pac = False
            for x, y in directions:
                dx, dy = x + i, y + j
                if 0<=dx<m and 0<=dy<n and heights[i][j] >= heights[dx][dy] and not visited[dx][dy]:
                    visited[dx][dy] = True
                    visit_pac = visit_pac or dfs_pac(dx,dy,visited)
            return visit_pac

        def dfs_atl(i: int,j: int,visited: list[list[bool]]):
            if i == 0 or j == 0:
                return True
            visit_atl = False
            for x, y in directions:
                dx, dy = x + i, y + j
                if 0<=dx<m and 0<=dy<n and heights[i][j] >= heights[dx][dy] and not visited[dx][dy]:
                    visited[dx][dy] = True
                    visit_atl = visit_atl or dfs_atl(dx,dy,visited)
            return visit_atl
        ans_pac = []
        ans_atl = []
        for i in range(m):
            for j in range(n):
                if dfs_pac(i,j,[[False]*n for _ in range(m)]):
                    ans_pac.append([i,j])
                if dfs_atl(i,j,[[False]*n for _ in range(m)]):
                    ans_atl.append([i,j])
        ans = [list(x) for x in (set(map(tuple, ans_atl)) & set(map(tuple, ans_pac)))]
        print(ans_atl,ans_pac)
        return ans


