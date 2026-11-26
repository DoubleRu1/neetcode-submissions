class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        m = sum(nums)
        if m % 2 == 1:
            return False
        visited = [False] * len(nums)
        def dfs(i):
            if i == 0:
                return True
            elif i < 0:
                return False
            for idx,num in enumerate(nums):
                if not visited[idx]:
                    visited[idx] = True
                    if dfs(i-num):
                        return True
                    visited[idx] = False
            print(i,visited)
            return False
        print(sum(nums)//2)
        return dfs(sum(nums)//2)
