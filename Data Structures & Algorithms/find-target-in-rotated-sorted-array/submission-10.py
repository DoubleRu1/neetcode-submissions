class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            mid_value = nums[mid]
            if mid_value == target:
                return mid
            if mid_value >= nums[0]:
                if target >= nums[0]:
                    if mid_value > target:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    left = mid + 1
            else:
                if target >= nums[0]:
                    right = mid - 1
                else:
                    if mid_value > target:
                        right = mid - 1
                    else:
                        left = mid + 1
        return -1