class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        psum = [0] * (n+2)
        psum[1] = nums[0]

        for i in range(1, n):
            psum[i+1] = nums[i]+psum[i]
        ans = [0] * n
        for i in range(len(nums)):
            right = psum[-2] - psum[i+1] - (nums[i] * (n-(i+1)))
            left = nums[i] * i - psum[i] 
            ans[i] = right + left
        return ans