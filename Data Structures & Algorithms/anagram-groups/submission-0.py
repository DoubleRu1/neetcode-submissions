class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_list.get(sorted_s,[]):
                sorted_list[sorted_s].append(s)
            else:
                sorted_list[sorted_s] = [s]

        return list(sorted_list.values())