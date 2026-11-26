class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums) 

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[mid] >= nums[0]:
                    if target > nums[0]:
                        right = mid
                    else:
                        left = mid
                else:
                    right = mid
            else:
                if nums[mid] >= nums[0]:
                    left = mid
                else:
                    if target > nums[0]:
                        right = mid
                    else:
                        left = mid
        if right == len(nums):
            right = 0
        if right < 0:
            return -1
        if nums[right] != target:
            return -1
        return right