class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        m = len(temperatures)
        ans = [0] * m
        for i in range(m-1,-1,-1):
            temp = temperatures[i]
            while stack and stack[-1][0] <= temp:
                stack.pop()
            ans[i] = stack[-1][1] - i if stack else 0
            stack.append((temp,i))
            print(stack)
            print(ans[i])
        return ans


