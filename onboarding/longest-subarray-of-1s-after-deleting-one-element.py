class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        last_seen = -1
        count = 0
        left = 0
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 0 and count == 1:
                left = last_seen + 1
                last_seen = i
            elif nums[i] == 0:
                last_seen = i  
                count = 1

            max_len = max(max_len, i - left)
 
        return max_len


            
