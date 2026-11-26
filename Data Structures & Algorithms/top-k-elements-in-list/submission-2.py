class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequents = collections.defaultdict(int)
        # for num in nums:
        #     frequents[str(num)] += 1
        frequents = collections.Counter(nums)
        frequents = list(zip(frequents.keys(),frequents.values()))
        frequents = sorted(frequents, key=lambda x: x[-1])
        return [int(item[0]) for item in frequents[-k:]]