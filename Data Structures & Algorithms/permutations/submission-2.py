class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = [False for _ in range(n)]
        path = []
        ans = []
        def backtrack(path, visited):
            if len(path) == n:
                ans.append(path.copy())
                return
            for i, num in enumerate(nums):
                if not visited[i]:
                    path.append(num)
                    visited[i] = True
                    backtrack(path, visited)
                    path.pop()
                    visited[i] = False
            return
        backtrack(path, visited)
        return ans