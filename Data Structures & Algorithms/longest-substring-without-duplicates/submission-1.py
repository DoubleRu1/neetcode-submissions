class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l, r = 0, 0
        n = len(s)
        s_dict = {}
        while r < n:
            s_dict[s[r]] = s_dict.get(s[r],0) + 1
            while l < r and s_dict[s[r]] > 1:
                s_dict[s[l]] = s_dict[s[l]] - 1
                l += 1
            r += 1

            ans = max(ans, r-l)
        
        return ans