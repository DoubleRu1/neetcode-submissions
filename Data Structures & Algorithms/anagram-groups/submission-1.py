class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = collections.defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            sorted_list[sorted_s].append(s)

        return list(sorted_list.values())