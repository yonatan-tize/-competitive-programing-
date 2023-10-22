class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        minSub = float('inf')
        total = 0

        for right in range (len(nums)):
            total += nums[right]  
            while total >= target:
                minSub = min(minSub, right- left + 1)
                total -= nums[left]
                left += 1
        return minSub if minSub != float('inf') else 0