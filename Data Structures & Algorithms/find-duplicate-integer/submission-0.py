class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        pre = 0
        for num in nums:
            if pre == num:
                return num
            pre = num