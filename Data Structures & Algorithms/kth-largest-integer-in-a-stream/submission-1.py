from heapq import heapify, heappush, heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [item for item in nums]
        heapify(self.heap)
        while len(self.heap)>self.k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap,val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        ans = heappop(self.heap)
        heappush(self.heap,ans)
        return ans
