class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        visited = [False for i in range(len(nums))]
        ans = []
        def backtrack(path,idx):
            ans.append(path.copy())
            for i in range(idx,len(nums)):
                if not visited[i]:
                    path.append(nums[i])
                    visited[i] = True
                    backtrack(path,i+1)
                    visited[i] = False
                    path.pop()
            return None
        
        backtrack([],0)
        print(ans)
        return ans 