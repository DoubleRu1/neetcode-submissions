class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(path,idx):
            if sum(path) == target:
                ans.append(path.copy())
                return None
            elif sum(path) > target:
                return None

            for i in range(idx,len(nums)):
                path.append(nums[i])
                backtrack(path,i)
                path.pop()
        
        backtrack([],0)
        return ans