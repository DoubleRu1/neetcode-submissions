class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = len(prices)
        if m < 2:
            return 0
        dp = [[0,0] for _ in range(m+1)]
        dp[1] = [-prices[0],0]
        dp[2] = [-min(prices[0],prices[1]),max(0, prices[1] + dp[1][0])]
        for i in range(3,m+1):
            dp[i][0] = max(
                dp[i-1][0],
                dp[i-2][1] - prices[i-1]
            )

            dp[i][1] = max(
                dp[i-1][1],
                dp[i-1][0] + prices[i-1]
            )
        # print(dp)
        return dp[-1][1]
