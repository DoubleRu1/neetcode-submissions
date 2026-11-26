class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        ans = 0
        while left < right:
            cur = min(heights[left], heights[right]) * (right - left)
            ans = max(ans,cur)
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return ans