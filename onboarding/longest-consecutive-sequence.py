class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n = set(nums)
        nums = sorted(list(n))
        count = 1
        ans = 0
        if len(nums) < 1:
            return ans
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] +1:
                count += 1
            else:
                ans = max(ans, count)
                count = 1
        ans = max(ans, count)
        return ans 
        
