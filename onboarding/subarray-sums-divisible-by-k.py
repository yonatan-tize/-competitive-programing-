class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        psum = 0
        sum_dict = {0:1}
        ans = 0
        for i in range(len(nums)):
            psum = (psum + nums[i]) % k
            if psum in sum_dict:
                ans += sum_dict[psum]
                sum_dict[psum] += 1 
            else:
                sum_dict[psum] = 1

        return ans


