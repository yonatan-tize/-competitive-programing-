class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        total = 0
        count = 0
        i = 0

        while total < n:
            if i < len(nums) and total + 1 >= nums[i]:
                total += nums[i]
                i += 1
            else:
                total += (total + 1)
                count += 1

        return count


                