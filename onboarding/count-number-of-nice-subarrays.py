class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count = 0
        nice_sub = 0
        left = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odd_count += 1
                count = 0
            while odd_count == k:
                if nums[left] % 2 == 1:
                    odd_count -= 1
                count += 1
                left += 1

            nice_sub += count 

        return nice_sub
                
                

