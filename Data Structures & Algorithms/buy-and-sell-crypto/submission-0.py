class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = float('inf')
        ans = 0
        for price in prices:
            cur = price - smallest
            smallest = min(smallest,price)
            ans = max(ans,cur)
        return ans