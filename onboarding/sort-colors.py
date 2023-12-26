class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        l = 0
        r = len(nums)-1

        while l <= r:
            if nums[l] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[l] == 1:
                l += 1
            else:
                nums[r], nums[l] = nums[l], nums[r]
                r -= 1

        