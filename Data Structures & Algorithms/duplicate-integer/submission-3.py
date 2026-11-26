class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for num in nums:
            if num_dict.get(num,0) == 1:
                return True
            num_dict[num] = num_dict.get(num,0) + 1
        return False