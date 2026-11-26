class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums)+2)
        a = [0,0]
        for item in nums:
            a.append(item)
        # print(a)
        for i in range(2,len(a)):
            dp[i] = max(dp[i-1],dp[i-2]+a[i])
        # print(dp)
        return dp[-1]