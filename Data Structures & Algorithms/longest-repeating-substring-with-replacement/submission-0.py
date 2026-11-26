class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        count = collections.defaultdict(int)
        ans = 0
        while right < len(s):
            print(left,right)
            count[s[right]] += 1
            while left < right and right + 1 - left - max(count.values()) > k:
                count[s[left]] -= 1
                left = left + 1
            ans = max(ans,right-left+1)
            right += 1
        return ans