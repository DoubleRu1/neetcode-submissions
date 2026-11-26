class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        path = []
        def backtrack(path,idx):
            total = sum(path)
            if total == target:
                ans.append(path.copy())
                return
            if total > target:
                return
            for i in range(idx, len(nums)):
                path.append(nums[i])
                backtrack(path, i)
                path.pop()
            return
        backtrack(path, 0)
        return ans