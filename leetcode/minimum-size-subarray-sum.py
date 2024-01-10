class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = 0
        l = 0
        min_len = len(nums) + 1
        for i in range(len(nums)):
            curr_sum += nums[i]
            
            while l <= i and curr_sum >= target:
                min_len = min(min_len, i-l+1)
                curr_sum -= nums[l]
                l += 1

        return min_len if min_len != len(nums) + 1 else 0