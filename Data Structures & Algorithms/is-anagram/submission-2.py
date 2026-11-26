class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_freq = {}
        for ch in s:
            char_freq[ch] = char_freq.get(ch,0) + 1
        for ch in t:
            char_freq[ch] = char_freq.get(ch,0) - 1
            if char_freq[ch] < 0:
                return False
        return True