class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = collections.defaultdict(int)
        for num in nums:
            if num_dict[str(num)]!=0:
                return True
            num_dict[str(num)] += 1
        return False