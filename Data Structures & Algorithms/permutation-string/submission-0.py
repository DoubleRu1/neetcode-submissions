from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        # Target is the character count of s1
        target = Counter(s1)
        left, right = 0, 0
        count = defaultdict(int)
        have = 0
        want = len(target)

        while right < len(s2):
            # Expand the window by including the right character
            count[s2[right]] += 1

            # If the current character count matches the target, increase have
            if count[s2[right]] == target[s2[right]]:
                have += 1

            # Shrink the window from the left if any character count exceeds the target
            while count[s2[right]] > target[s2[right]]:
                count[s2[left]] -= 1
                if count[s2[left]] == target[s2[left]] - 1:
                    have -= 1
                left += 1
            
            # If all characters are matched, return True
            if have == want:
                return True
            
            # Move the right pointer to expand the window
            right += 1
        
        return False
