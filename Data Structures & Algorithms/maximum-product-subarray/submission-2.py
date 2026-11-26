class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[0,0] for _ in range (len(nums))]
        dp[0][0] = dp[0][1] = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > 0:
                dp[i][0] = max(dp[i-1][0] * nums[i], nums[i])
                dp[i][1] = dp[i-1][1] * nums[i]
            else:
                dp[i][0] = dp[i-1][1] * nums[i]
                dp[i][1] = min(dp[i-1][0] * nums[i],nums[i])
            ans = max(ans, dp[i][0])
        print(dp)
        return ans