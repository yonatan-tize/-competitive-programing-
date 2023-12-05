class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)-1, 1, -1):
            if nums[i] < nums[i-1] + nums[i-2]:
                return nums[i] + nums[i-1] + nums[i-2]
        return 0











        # for j in range(len(nums)-1, 1, -1):
        #     num = nums[j]
        #     i = 0
        #     k = j - 1
        #     while i < k:
        #         if nums[i] + nums[k] > num:
        #             ans = max(ans, nums[k-1] + nums[k] + num)
        #             break
        #         else:
        #             i += 1
        # return ans
            
                
