class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        l = 1
        ans = nums[0]
        total = nums[0]

        while l < len(nums):
            total += nums[l]
            if math.ceil(total / (l+1)) > ans:
                ans =  math.ceil(total / (l+1)) 

            l += 1

        return ans 