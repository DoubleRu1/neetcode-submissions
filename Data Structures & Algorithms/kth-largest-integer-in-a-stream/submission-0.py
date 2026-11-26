from heapq import heapify, heappush, heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [-item for item in nums]
        heapify(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap,-val)
        temp = [0] * self.k
        
        for i in range(self.k):
            temp[i] = heappop(self.heap)
        for i in range(self.k):
            heappush(self.heap,temp[i])
        print(temp)
        return -temp[-1]
