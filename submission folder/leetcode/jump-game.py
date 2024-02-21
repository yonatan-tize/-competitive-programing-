class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        curr_max = nums[0]
        if len(nums) == 1:
            return True

        for i in range(len(nums)):
            if curr_max == 0:
                return False
            curr_max = max(nums[i], curr_max-1)  

        return True

        