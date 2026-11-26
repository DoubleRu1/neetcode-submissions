class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #没有环
        graph = {}
        for edge in edges:
            if graph.get(edge[0],[]) == []:
                graph[edge[0]] = [edge[1]]
            else:
                graph[edge[0]].append(edge[1])
            
            if graph.get(edge[1],[]) == []:
                graph[edge[1]] = [edge[0]]
            else:
                graph[edge[1]].append(edge[0])
        print(graph)
        if not graph:
            return True
        visited = [False] * n
        def dfs(i,j):
            if not visited[i]:
                visited[i] = True
            else:
                return False
            for neibor in graph[i]:
                    if neibor == j:
                        continue
                    if not dfs(neibor,i):
                        return False
            return True
        # print(visited)
        return dfs(0,-1) and all(visited)

            
