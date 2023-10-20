class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = - float('inf')
        total = sum(nums[:k-1])
        i = k - 1
        n = len(nums)

        while i < n:
            total += nums[i]
            max_avg = max(max_avg, total / k)
            i += 1
            total -= nums[i-k]

        return max_avg






        