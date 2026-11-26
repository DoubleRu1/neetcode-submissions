class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curmax = 0
        for idx in range(len(nums)):
            if idx <= curmax:
                curmax = max(curmax,nums[idx]+idx)
            else:
                break
        return True if curmax >= len(nums) - 1 else False