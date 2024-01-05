class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k-1])
        ans = -float('inf')
        i = k-1
        for i in range(k-1, len(nums)):
            total += nums[i]
            ans = max(ans, total/k)
            total -= nums[i-k+1]
        return ans
