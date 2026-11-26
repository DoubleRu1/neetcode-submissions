class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # define a dp to represent current maxsum in each position
        cursum = [0] * (len(nums) + 1)
        for idx in range(1,len(nums)+1):
            cursum[idx] = max(cursum[idx-1] + nums[idx-1],nums[idx-1])

        print(cursum)

        return max(cursum[1:])