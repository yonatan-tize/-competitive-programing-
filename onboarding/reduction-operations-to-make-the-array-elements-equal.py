class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        l = n - 1
        while l > 0:
            while l > 0 and nums[l] == nums[l-1]:
                l -= 1
            if l == 0 and nums[0] == nums[1]:
                break
            count += n - l
            l -= 1
        return count


            
