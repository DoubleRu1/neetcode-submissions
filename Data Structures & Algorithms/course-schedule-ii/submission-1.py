class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for item in prerequisites:
            graph[item[1]].append(item[0])
            indegree[item[0]] += 1
        # print(graph,indegree)
        q = [i for i in range(numCourses) if indegree[i]==0]
        ans = []
        while q:
            idx = q.pop()
            ans.append(idx)
            for i in graph[idx]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
                graph[idx] = []
        if len(ans) == numCourses:
            return ans
        else:
            return []