class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m = len(nums)
        left, right = -1, m
        while left < right-1:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        return -1
