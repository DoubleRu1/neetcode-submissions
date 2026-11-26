class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for e in prerequisites:
            graph[e[1]].append(e[0])
            in_degree[e[0]] += 1
        q = [i for i, num in enumerate(in_degree) if num == 0]
        target = 0
        while q:
            node = q.pop()
            target+=1
            for next_node in graph[node]:
                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    q.append(next_node)
            graph[node] = []
        return target == numCourses
