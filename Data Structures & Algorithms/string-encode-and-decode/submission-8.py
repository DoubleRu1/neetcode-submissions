class Solution:
    def encode(self, strs: List[str]) -> str:
        return ''.join([str(len(s)) + '#' + s for s in strs])
        
    def decode(self, s: str) -> List[str]:
        print(s)
        ans = []
        i=0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            count = int(s[i:j])
            i = j + 1
            j = i + count
            ans.append(s[i:j])
            i = j
        return ans


