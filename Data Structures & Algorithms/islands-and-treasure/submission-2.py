import collections
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(i:int,j:int,dis:int,visited:list[list[bool]]) -> None:
            queue = collections.deque([(i,j)])
            dis = 0
            while queue:
                # print(queue)
                temp = collections.deque()
                while queue:
                    headx, heady = queue.popleft()
                    for x,y in directions:
                        dx, dy = headx+x, heady+y
                        if 0<=dx<m and 0<=dy<n and not visited[dx][dy]:
                            if  grid[dx][dy] != 0 and grid[dx][dy] != -1:
                                grid[dx][dy] = min(grid[dx][dy],dis+1)
                                visited[dx][dy] = True
                                temp.append((dx,dy))
                queue = temp
                dis += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    visited = [[False] * n for _ in range(m)]
                    dfs(i,j,0,visited)
        # print(grid)

