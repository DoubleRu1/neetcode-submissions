class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path = []
        ans = []
        def backtrack(path,idx):
            ans.append(path.copy())
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(path, i+1)
                path.pop()
        backtrack(path, 0)
        return ans