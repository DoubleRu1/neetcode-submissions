class Solution:
    def jump(self, nums: List[int]) -> int:
        def dp(idx:int) -> int:
            if idx == 0:
                return 0
            cur_min = float('inf')
            for i in range(idx-1,-1,-1):
                if nums[i] >= idx - i:
                    cur_min = min(dp(i)+1,cur_min)
            print(idx,cur_min)
            return cur_min
        
        return dp(len(nums)-1)