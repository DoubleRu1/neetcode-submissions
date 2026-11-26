class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if not n > 0:
            return 0
        left, right = 0, 0
        window = {}
        ans = 1
        while right < n:
            window[s[right]] = window.get(s[right],0) + 1
            right += 1
            while left < right and (sum(window.values()) - max(window.values())) > k:
                window[s[left]] -= 1
                if window[s[left]]==0:
                    window.pop(s[left])
                left += 1
            ans = max(ans, right - left)
        return ans