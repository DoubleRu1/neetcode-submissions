class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequents = collections.defaultdict(int)
        for num in nums:
            frequents[str(num)] += 1
        frequents = list(zip(frequents.keys(),frequents.values()))
        print(frequents)
        frequents = sorted(frequents, key=lambda x: x[-1])
        return [int(item[0]) for item in frequents[-k:]]