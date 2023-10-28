class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        psum = 0
        d = {0:1}

        for i in range(len(nums)):
            psum = (psum + nums[i]) % k
            if psum in d:
                ans += d[psum]
                d[psum] += 1 
            else:
                d[psum] = 1

        return ans
