class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary(nums, target,start):
            left = 0
            ans = -1
            right = len(nums)-1

            while left <= right:
                mid = (right + left) // 2
                if nums[mid] > target:
                    right = mid - 1

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    if start:
                        right = mid - 1
                        ans = mid
                    else:
                        left = mid + 1
                        ans = mid
            return ans

        left = binary(nums, target,True)
        right = binary(nums, target, False)
        return [left, right]
