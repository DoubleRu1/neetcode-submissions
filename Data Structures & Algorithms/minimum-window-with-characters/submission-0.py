class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        target = collections.Counter(t)
        window = {}
        want = len(target)
        have = 0
        ans = float('inf')
        minleft,minright = float('-inf'), float('inf')
        while right < len(s):
            if s[right] in target:
                window[s[right]] = window.get(s[right],0) + 1
                if window[s[right]] == target[s[right]]:
                    have += 1
            while have == want:
                if right - left + 1 < ans:
                    ans = right - left + 1
                    minleft = left
                    minright = right
                if s[left] in target:
                    window[s[left]] = window[s[left]] - 1
                    if window[s[left]] == target[s[left]]-1:
                        have -= 1
                left += 1
            right += 1
        return s[minleft:minright+1] if minleft != float('-inf') and minright != float('inf') else ''
        