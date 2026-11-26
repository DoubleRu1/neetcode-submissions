class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def backtrack(path,idx):
            if idx == len(nums):
                if path not in ans:
                    ans.append(path.copy())
                return
            i = idx
            pre = nums[idx]
            while i < len(nums):
                path.append(nums[i])
                i += 1
                # while i < len(nums) and nums[i] == pre:
                #     i += 1
                backtrack(path,i)
                path.pop()
                backtrack(path,i)
        backtrack([],0)
        return ans