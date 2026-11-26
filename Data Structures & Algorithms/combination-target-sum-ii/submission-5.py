class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        path = []
        ans = []
        def backtrack(path, idx):
            total = sum(path)
            if total == target:
                ans.append(path.copy()) 
                return
            if total > target:
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(path, i+1)
                path.pop()
            return
        backtrack(path, 0)
        return ans