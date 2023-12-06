class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        failed_count = 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                failed_count += 1
                if i>=2 and nums[i-2]>nums[i]:
                    nums[i] = nums[i-1]
                if failed_count == 2:
                    return False
        return True
        