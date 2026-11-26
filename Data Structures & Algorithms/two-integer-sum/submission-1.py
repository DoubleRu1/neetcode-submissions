class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for idx, num in enumerate(nums):
            target_idx = num_dict.get(target-num,-1)
            if  target_idx != -1:
                return [target_idx,idx]
            num_dict[num] = idx
        return None
