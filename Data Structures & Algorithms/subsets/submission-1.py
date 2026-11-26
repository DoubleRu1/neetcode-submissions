class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = [False for _ in range (len(nums))]
        path = []
        def backtrack(path, idx):
            ans.append(path.copy())
            for i in range(idx,len(nums)):
                num = nums[i]
                if not visited[i]:
                    visited[i] = True
                    path.append(num)
                    backtrack(path, i+1)
                    path.pop()
                    visited[i] = False
            return 
        backtrack(path, 0)
        return ans