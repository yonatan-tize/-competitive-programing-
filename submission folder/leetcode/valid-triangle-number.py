class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        valid_num = 0
        size = len(nums)

        for i in range(size-1, 1, -1):
            left = 0
            right = i-1

            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    valid_num += (right - left)
                    right -= 1
                else:
                    left += 1

        return valid_num

            


