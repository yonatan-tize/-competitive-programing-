class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        psum = [0] * len(nums)

        for start, end in requests:
            psum[start] += 1
            if end != len(nums)-1:
                psum[end+1] -= 1 
        for i in range(1, len(psum)):
            psum[i] += psum[i-1]
        nums.sort()
        psum.sort()
        total = 0
        n = 1e9 + 7
        for i in range(len(psum)):
            total += (nums[i]*psum[i]) 
        
        return int(total % n)