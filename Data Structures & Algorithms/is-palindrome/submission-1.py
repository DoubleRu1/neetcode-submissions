class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip('?')
        s = [item.lower() for item in s if 'a'<=item.lower()<='z' or '0'<=item<='9']
        s = ''.join(s)
        print(s)
        m = len(s)
        for i in range(m//2):
            if s[i] != s[m-1-i]:
                print(i)
                return False
        return True
