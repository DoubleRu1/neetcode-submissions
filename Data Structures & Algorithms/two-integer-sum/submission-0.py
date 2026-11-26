class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cur_dict = collections.defaultdict(list)
        for idx, num in enumerate(nums):
            need = target - num
            if cur_dict[need] != []:
                return [cur_dict[need][0],idx]
            cur_dict[num].append(idx)
        return []

