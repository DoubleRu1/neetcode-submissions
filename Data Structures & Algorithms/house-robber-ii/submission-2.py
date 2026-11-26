class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def get_max(nums):
            dp = [0] * (len(nums)+2)

            for i in range(2,len(nums)+2):
                dp[i] = max(dp[i-1],dp[i-2] + nums[i-2])
            return dp[-1]
        m1 = get_max(nums[:-1])
        m2 = get_max(nums[1:])

        return max(m1,m2)