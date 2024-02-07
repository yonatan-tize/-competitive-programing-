class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_product = [1] * len(nums)

        for i in range(1,len(nums)):
            pre_product[i] = nums[i-1] * pre_product[i-1]

        m = nums[-1]
        for j in range(len(nums)-2, -1 , -1):
            pre_product[j] *= m
            m *= nums[j]

        return pre_product
