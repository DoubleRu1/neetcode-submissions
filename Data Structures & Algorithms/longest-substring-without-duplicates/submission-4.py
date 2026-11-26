class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if not n > 0:
            return 0
        left, right = 0, 1
        window = {s[0]:1}
        ans = 1
        while right < n:
            while left < right and window.get(s[right],0) > 0:
                window[s[left]] -= 1
                left += 1
            window[s[right]] = window.get(s[right],0) + 1
            right += 1
            ans = max(ans, right - left)
        return ans
