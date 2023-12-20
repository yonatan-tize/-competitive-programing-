class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
                j += 1
        return count
