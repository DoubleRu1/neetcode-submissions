class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for s in strs:
            s_list = [0] * 26
            for ch in s:
                s_list[ord(ch)-ord('a')]+=1
            if anagram_dict.get(tuple(s_list),[]):
                anagram_dict[tuple(s_list)].append(s)
            else:
                anagram_dict[tuple(s_list)] = [s]
        
        return list(anagram_dict.values())
            
