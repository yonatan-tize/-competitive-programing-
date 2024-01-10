class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        curr_sum = 0
        max_sum = 0
        left = 0
        for right, num in enumerate(nums):
            while num in seen:
                curr_sum -= nums[left]
                seen[nums[left]] -= 1
                del seen[nums[left]] 
                left += 1

            seen[num] = 1
            curr_sum += num
            max_sum = max(max_sum, curr_sum)

        return max_sum

