class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = collections.defaultdict(int)
        for num in nums:
            sequence[num] += 1
        ans = 0

        for key, _ in sequence.items():
            if sequence.get(key-1,0) == 0:
                cur = 0
                start = key
                while sequence.get(start,0) != 0:
                    cur += 1
                    start += 1
                ans = max(ans,cur)

        return ans

            

