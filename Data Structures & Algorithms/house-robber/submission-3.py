class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [[0,0] for _ in range(n)]
        dp[0] = [nums[0],0]
        dp[1] = [nums[1],nums[0]]
        for i in range(2, n):
            dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + nums[i]
            dp[i][1] = max(dp[i-1][0], dp[i-1][1])
        print(dp)
        return max(dp[-1])
