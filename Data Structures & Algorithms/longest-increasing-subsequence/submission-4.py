class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        m = len(nums)
        dp = [1] * (m)
        for i,num in enumerate(nums):
            for j in range(i):
                if num > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        # print(dp)
        return max(dp)
