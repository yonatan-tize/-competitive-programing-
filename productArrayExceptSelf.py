class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        for i in range(1,len(nums)):
            left[i] = nums[i-1] * left[i-1] 
        
        m = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            left[i] *= m
            m *= nums[i]

        return left