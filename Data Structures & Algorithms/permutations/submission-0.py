class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        ans = []
        visited = [False] * length
        def backtrack(path):
            if len(path) == length:
                ans.append(path.copy())
            
            for i in range(length):
                if not visited[i]:
                    path.append(nums[i])
                    visited[i] = True
                    backtrack(path)
                    visited[i] = False
                    path.pop()
        backtrack([])

        return ans
