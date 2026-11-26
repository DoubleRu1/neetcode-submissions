class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_product = [1]
        post_product = [1]
        for num in nums[:len(nums)-1]:
            pre_product.append(pre_product[-1]*num)
        for idx in range(len(nums)-1,0,-1):
            post_product.append(post_product[-1]*nums[idx])
        for idx in range(len(nums)//2):
            temp = post_product[idx]
            post_product[idx] = post_product[len(nums)-idx-1]
            post_product[len(nums)-idx-1] = temp
        # print(pre_product)
        # print(post_product)
        answer = []
        for i in range(len(nums)):
            answer.append(pre_product[i]*post_product[i])
        return answer
