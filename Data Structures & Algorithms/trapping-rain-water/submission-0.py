class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        left_stack = [0] * n
        left_stack[0] = height[0]
        for i in range(1,n):
            left_stack[i] = max(left_stack[i-1],height[i])
        
        right_stack = [0] * n
        right_stack[-1] = height[-1]
        for i in range(n-2,-1,-1):
            right_stack[i] = max(right_stack[i+1],height[i])
        res = 0

        for i in range(n):
            res += min(left_stack[i],right_stack[i]) - height[i]
        return res