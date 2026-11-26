class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i, t in enumerate(nums):
            j, k = i+1, n-1
            while j < k:
                s = t + nums[j] + nums[k]
                if s == 0:
                    if [t,nums[j],nums[k]] not in ans:
                        ans.append([t,nums[j],nums[k]])
                    j += 1
                    # print(ans,s)
                elif s > 0:
                    k -= 1
                else:
                    j += 1
        return ans


