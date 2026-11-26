class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = collections.Counter(s)
        t_dict = collections.Counter(t)
        if len(s_dict) != len(t_dict):
            return False
        for key, value in s_dict.items():
            target = t_dict.get(key,0)
            if value != target:
                return False
        return True