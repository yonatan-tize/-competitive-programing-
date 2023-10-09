class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, j = 0, len(nums) - 1
        k = 0

        while k <= j:
            num = nums[k]
            if num == 1:
                k += 1
            elif num == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
                k += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                j -= 1
                
        