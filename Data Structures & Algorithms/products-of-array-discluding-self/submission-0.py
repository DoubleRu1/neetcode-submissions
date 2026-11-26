class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = len(nums)
        product = [0] * m
        product[0] = 0
        product[1] = nums[0]
        for i in range(2,m):
            product[i] = product[i-1] * nums[i-1]
        reverse_product = [0] * m
        reverse_product[-1] = 0
        reverse_product[-2] = nums[-1]
        for i in range(m-3,-1,-1):
            reverse_product[i] = reverse_product[i+1] * nums[i+1]

        ans = [0] * m
        ans[0] = reverse_product[0]
        ans[-1] = product[-1]
        for i in range(1,m-1):
            ans[i] = reverse_product[i] * product[i]
        return ans

        