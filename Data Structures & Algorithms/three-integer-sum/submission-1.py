class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = list(sorted(nums))
        print(nums)
        m = len(nums)
        ans = []
        for i in range(m):
            j, k = i+1, m-1
            target = -nums[i]
            while j < k:
                print('***' * 10)
                print(i,j,k)
                print(target)
                cur = nums[j] + nums[k]
                if cur == target:
                    item = [nums[i],nums[j],nums[k]]
                    if item not in ans:
                        ans.append(item)
                    j += 1
                    k -= 1
                elif cur < target:
                    j += 1
                else:
                    k -= 1
                print(i,j,k)
                print('***' * 10)
        return ans