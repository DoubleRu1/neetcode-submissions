class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []
        def backtrack(start, remain):
            if remain == 0:
                ans.append(path.copy())
            elif remain < 0:
                return None
            idx = start
            while idx < len(candidates):
                
                while start<idx<len(candidates) and candidates[idx] == candidates[idx-1]:
                    idx += 1
                if idx < len(candidates):
                    path.append(candidates[idx])
                    backtrack(idx+1,remain-candidates[idx])
                    path.pop()
                    idx += 1

        backtrack(0,target)
        return ans
                

