from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = len(coins)
        
        @cache
        def backtrack(total, i):
            if total == amount:
                return 1
            elif total > amount:
                return 0
            ans = 0
            for idx in range(i, m):
                ans += backtrack(total+coins[idx], idx)
            return ans
        return backtrack(0, 0)