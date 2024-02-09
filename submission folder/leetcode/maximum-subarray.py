class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = -float('inf')
        psum = 0

        for i in range(len(nums)):
            psum += nums[i]
            if psum > curr_max:
                curr_max = psum

            if psum < 0:
                psum = 0

        return curr_max

            