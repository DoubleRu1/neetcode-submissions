class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        if length == 0:
            return 0
        elif length == 1 or length == 2:
            return max(cost)
        dp = [0] *(length + 1)
        dp[0] = 0
        dp[1] = 0

        for i in range(2,length+1):
            dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        # print(dp)
        return dp[-1]