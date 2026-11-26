

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        l = len(nums)
        if l == 0:
            return 0

        dp = [{} for _ in range(l)]
        # 处理 nums[0] == 0 的情况
        dp[0] = {nums[0]: 1}
        dp[0][-nums[0]] = dp[0].get(-nums[0], 0) + 1

        for i in range(1, l):
            for k, v in dp[i - 1].items():
                dp[i][k + nums[i]] = dp[i].get(k + nums[i], 0) + v
                dp[i][k - nums[i]] = dp[i].get(k - nums[i], 0) + v

        return dp[-1].get(target, 0)
