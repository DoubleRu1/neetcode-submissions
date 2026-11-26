class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 单调栈，下一个比自己小的元素
        m = len(heights)
        left_stack = []
        left = [m] * m
        for idx in range(m):
            item = heights[idx]
            while left_stack and item < heights[left_stack[-1]]:
                i = left_stack.pop()
                left[i] = idx
            left_stack.append(idx)
        print(left)

        right = [-1] * m
        right_stack = []
        for idx in range(m-1,-1,-1):
            item = heights[idx]
            while right_stack and item < heights[right_stack[-1]]:
                i = right_stack.pop()
                right[i] = idx
            right_stack.append(idx)
        print(right)

        ans = 0
        for i in range(m):
            ans = max(ans,(left[i]-right[i]-1) * heights[i])
        return ans

