class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right
        while left <= right:
            mid = (left+right) // 2
            current = sum([(item+mid-1) // mid for item in piles])
            print(mid,current)
            # print(current)
            if current <= h:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        
        return ans 
