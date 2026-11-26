class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        length = len(s)
        strings = {}
        ans = 0
        while right < length:
            ch_r = s[right]
            strings[ch_r] = strings.get(ch_r,0) + 1
            while strings[ch_r] > 1:
                strings[s[left]] -= 1
                left += 1
            right += 1
            ans = max(ans,right - left)
            print(left,right,ans,strings)
        return ans