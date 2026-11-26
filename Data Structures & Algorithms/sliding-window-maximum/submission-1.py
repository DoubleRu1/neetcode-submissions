class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left, right = 0, 0
        window = []
        ans = []
        while right < len(nums):
            if right - left < k:
                heapq.heappush(window,-nums[right])
                if right - left == k-1:
                    top = heapq.heappop(window)
                    ans.append(-top)
                    heapq.heappush(window,top)
            else:
                # print(left,right)
                window.remove(-nums[left])
                heapq.heappush(window,-nums[right])
                left += 1
                # print(window,left,right)
                heapq.heapify(window)
                top = heapq.heappop(window)
                ans.append(-top)
                heapq.heappush(window,top)
            right += 1
        return ans


