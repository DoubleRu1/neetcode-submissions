import collections
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)

        tuple_num = [
            (count, num)
            for num, count in counts.items()
        ]
        heap = []
        for tn in tuple_num:
            heapq.heappush(heap,tn)
            if len(heap) > k:
                heapq.heappop(heap)
            # print(heap)
        return [item[1] for item in heap]